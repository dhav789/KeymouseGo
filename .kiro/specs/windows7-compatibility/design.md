# Design Document: Windows 7 Compatibility Refactoring

## Overview

本设计文档描述了将 KeymouseGo 项目重构为支持 Windows 7 的技术方案。主要工作包括：

1. 将 GUI 框架从 PySide6 降级为 PySide2
2. 移除或替换 qt-material 主题库
3. 更新所有相关的 API 调用和导入语句
4. 处理 PySide2 中不存在或 API 不同的功能

## Architecture

### 当前架构

```
┌─────────────────────────────────────────────────────────┐
│                    KeymouseGo.py                        │
│                    (主入口)                              │
└─────────────────────────────────────────────────────────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
┌─────────────────┐ ┌─────────────┐ ┌─────────────────┐
│    UIFunc.py    │ │ Recorder/   │ │    Event/       │
│  (UI 逻辑层)     │ │ (录制模块)   │ │  (事件处理)      │
└─────────────────┘ └─────────────┘ └─────────────────┘
         │                 │
         ▼                 ▼
┌─────────────────┐ ┌─────────────────┐
│   UIView.py     │ │   Util/         │
│ (UI 视图层)      │ │ (工具类)        │
└─────────────────┘ └─────────────────┘
```

### 重构后架构

架构保持不变，仅替换底层依赖：

- PySide6 → PySide2
- qt-material → Qt 原生样式表
- QSoundEffect → QSound 或 pygame.mixer

## Components and Interfaces

### 1. 需要修改的文件

| 文件 | 修改内容 |
|------|----------|
| `KeymouseGo.py` | PySide6 → PySide2 导入 |
| `UIFunc.py` | PySide6 → PySide2，移除 qt-material |
| `UIView.py` | 重新生成 PySide2 版本 |
| `UIFileDialogFunc.py` | PySide6 → PySide2 导入 |
| `UIFileDialogView.py` | 重新生成 PySide2 版本 |
| `Recorder/__init__.py` | PySide6 → PySide2 导入 |
| `Util/RunScriptClass.py` | PySide6 → PySide2 导入 |
| `requirements-windows.txt` | 更新依赖版本 |
| `requirements-universal.txt` | 更新依赖版本 |

### 2. API 差异处理

#### 2.1 QSoundEffect 替换

PySide2 的 QSoundEffect 在 QtMultimedia 中，但 API 略有不同：

```python
# PySide6
from PySide6.QtMultimedia import QSoundEffect
player = QSoundEffect()
player.setSource(QUrl.fromLocalFile(path))
player.play()

# PySide2 替代方案 - 使用 QSound
from PySide2.QtMultimedia import QSound
QSound.play(path)
```

#### 2.2 Signal 定义差异

```python
# PySide6
updateStateSignal: Signal = Signal(State)

# PySide2 (相同语法，但需要从 PySide2.QtCore 导入)
from PySide2.QtCore import Signal
updateStateSignal = Signal(State)
```

#### 2.3 QIcon.Mode 枚举

```python
# PySide6
icon.addFile(path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)

# PySide2
icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
```

#### 2.4 exec() vs exec_()

```python
# PySide6
app.exec()

# PySide2
app.exec_()
```

### 3. 主题系统重构

移除 qt-material，使用 Qt 原生样式表：

```python
# 移除
from qt_material import list_themes, QtStyleTools

# 替换为简单的样式表系统
THEMES = {
    'Default': '',
    'Dark': '''
        QWidget { background-color: #2b2b2b; color: #ffffff; }
        QPushButton { background-color: #3c3c3c; border: 1px solid #555; }
    ''',
    'Light': '''
        QWidget { background-color: #f0f0f0; color: #000000; }
        QPushButton { background-color: #e0e0e0; border: 1px solid #ccc; }
    '''
}
```

## Data Models

### 配置文件格式

配置文件 `config.ini` 保持不变，使用 QSettings 读写：

```ini
[Config]
StartHotKey=f6
StopHotKey=f9
RecordHotKey=f10
LoopTimes=1
Precision=200
Language=zh-cn
Theme=Default
```

### 脚本文件格式

脚本文件格式 (JSON5) 保持不变：

```json5
{
  scripts: [
    {type: "event", event_type: "EM", delay: 3000, action_type: "mouse left down", action: ["0.05208%", "0.1852%"]},
    {type: "event", event_type: "EK", delay: 1000, action_type: "key down", action: [70, 'F', 0]}
  ]
}
```

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system-essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Configuration Round-Trip Consistency

*For any* valid configuration dictionary, serializing it to INI format and then deserializing should produce an equivalent configuration dictionary.

**Validates: Requirements 2.5**

### Property 2: UI Widget Interaction Consistency

*For any* UI widget (combo box, slider, spinbox) and any valid value within its range, setting the value programmatically should result in the widget reporting that same value when queried.

**Validates: Requirements 6.2, 6.3**

### Property 3: Import Statement Correctness

*For any* Python source file in the project, all Qt-related imports should reference PySide2 modules and not PySide6 modules.

**Validates: Requirements 2.1, 2.2, 2.3, 2.4, 4.1, 4.2, 4.3**

## Error Handling

### 1. 导入错误处理

```python
try:
    from PySide2.QtWidgets import QApplication
except ImportError:
    print("PySide2 is required. Please install: pip install PySide2")
    sys.exit(1)
```

### 2. 音频播放错误处理

```python
def playtune(self, filename: str):
    try:
        path = get_assets_path('sounds', filename)
        if os.path.exists(path):
            QSound.play(path)
    except Exception as e:
        logger.warning(f"Failed to play sound: {e}")
```

### 3. 主题应用错误处理

```python
def apply_theme(self, theme_name: str):
    try:
        stylesheet = THEMES.get(theme_name, '')
        self.app.setStyleSheet(stylesheet)
    except Exception as e:
        logger.warning(f"Failed to apply theme: {e}")
        self.app.setStyleSheet('')  # 回退到默认主题
```

## Testing Strategy

### 单元测试

使用 pytest 进行单元测试：

1. 测试配置文件读写
2. 测试主题应用
3. 测试 UI 组件初始化

### 属性测试

使用 hypothesis 进行属性测试：

```python
from hypothesis import given, strategies as st

@given(st.dictionaries(
    keys=st.sampled_from(['StartHotKey', 'StopHotKey', 'LoopTimes']),
    values=st.text(min_size=1, max_size=20)
))
def test_config_roundtrip(config_dict):
    """
    **Feature: windows7-compatibility, Property 1: Configuration Round-Trip Consistency**
    """
    # Serialize to INI format
    serialized = serialize_config(config_dict)
    # Deserialize back
    deserialized = deserialize_config(serialized)
    # Verify equality
    assert config_dict == deserialized
```

### 集成测试

1. 在 Windows 7 虚拟机中运行应用
2. 验证所有 UI 功能正常工作
3. 验证录制和回放功能

### 测试框架配置

- 属性测试库：hypothesis
- 单元测试框架：pytest
- 每个属性测试运行至少 100 次迭代

# Requirements Document

## Introduction

本项目旨在重构 KeymouseGo（一个鼠标键盘录制回放工具）以支持 Windows 7 操作系统。当前版本使用 PySide6 和 qt-material，这些依赖不支持 Windows 7。需要将 GUI 框架降级为 PySide2/PyQt5，并替换或移除不兼容的依赖。

## Glossary

- **KeymouseGo**: 鼠标键盘操作录制和回放工具
- **PySide6**: Qt 6 的 Python 绑定，不支持 Windows 7
- **PySide2**: Qt 5 的 Python 绑定，支持 Windows 7
- **PyQt5**: Qt 5 的另一个 Python 绑定，支持 Windows 7
- **qt-material**: 基于 Material Design 的 Qt 主题库
- **Windows 7**: Microsoft Windows 7 操作系统（2009年发布）

## Requirements

### Requirement 1

**User Story:** As a Windows 7 user, I want to run KeymouseGo on my system, so that I can record and replay mouse/keyboard actions.

#### Acceptance Criteria

1. WHEN the application starts on Windows 7 THEN the System SHALL display the main GUI window without errors
2. WHEN the user clicks the Record button THEN the System SHALL begin recording mouse and keyboard events
3. WHEN the user clicks the Launch button THEN the System SHALL replay the recorded script
4. WHEN the application runs on Windows 7 THEN the System SHALL maintain all existing functionality from the current version

### Requirement 2

**User Story:** As a developer, I want to replace PySide6 with a Windows 7 compatible Qt binding, so that the GUI framework works on older systems.

#### Acceptance Criteria

1. WHEN the application imports Qt modules THEN the System SHALL use PySide2 instead of PySide6
2. WHEN the application uses Qt widgets THEN the System SHALL use PySide2.QtWidgets module
3. WHEN the application uses Qt core functionality THEN the System SHALL use PySide2.QtCore module
4. WHEN the application uses Qt multimedia THEN the System SHALL use PySide2.QtMultimedia module
5. WHEN the application serializes configuration THEN the System SHALL use JSON format for round-trip consistency

### Requirement 3

**User Story:** As a developer, I want to replace or remove qt-material theme library, so that the application can run without PySide6 dependencies.

#### Acceptance Criteria

1. WHEN the application applies themes THEN the System SHALL use a PySide2-compatible theming approach
2. WHEN the user selects a theme THEN the System SHALL apply the theme using Qt stylesheets
3. WHEN the Default theme is selected THEN the System SHALL display the native Qt appearance

### Requirement 4

**User Story:** As a developer, I want to update all import statements and API calls, so that the code is compatible with PySide2.

#### Acceptance Criteria

1. WHEN the code imports from PySide6.QtWidgets THEN the System SHALL import from PySide2.QtWidgets instead
2. WHEN the code imports from PySide6.QtCore THEN the System SHALL import from PySide2.QtCore instead
3. WHEN the code imports from PySide6.QtGui THEN the System SHALL import from PySide2.QtGui instead
4. WHEN the code uses QSoundEffect THEN the System SHALL use an alternative audio playback method compatible with PySide2
5. WHEN the code uses Signal/Slot decorators THEN the System SHALL use PySide2-compatible syntax

### Requirement 5

**User Story:** As a developer, I want to update the requirements files, so that users can install the correct dependencies for Windows 7.

#### Acceptance Criteria

1. WHEN a user installs dependencies on Windows 7 THEN the System SHALL install PySide2 instead of PySide6
2. WHEN a user installs dependencies THEN the System SHALL install a Python version compatible with Windows 7 (Python 3.8 or earlier recommended)
3. WHEN the requirements file is parsed THEN the System SHALL list all dependencies with compatible versions

### Requirement 6

**User Story:** As a user, I want the application to have a functional UI on Windows 7, so that I can use all features.

#### Acceptance Criteria

1. WHEN the main window displays THEN the System SHALL show all buttons, labels, and input fields correctly
2. WHEN the user interacts with combo boxes THEN the System SHALL respond to selection changes
3. WHEN the user adjusts sliders and spinboxes THEN the System SHALL update values correctly
4. WHEN the user views the text log THEN the System SHALL display recorded actions in real-time

### Requirement 7

**User Story:** As a developer, I want to regenerate UI files for PySide2, so that the UI code is compatible.

#### Acceptance Criteria

1. WHEN the UIView.py is generated THEN the System SHALL use PySide2 imports
2. WHEN the UIFileDialogView.py is generated THEN the System SHALL use PySide2 imports
3. WHEN UI files are compiled THEN the System SHALL produce Python code compatible with PySide2

### Requirement 8

**User Story:** As a user, I want hotkey functionality to work on Windows 7, so that I can control recording and playback with keyboard shortcuts.

#### Acceptance Criteria

1. WHEN the user presses the start hotkey THEN the System SHALL begin script execution
2. WHEN the user presses the stop hotkey THEN the System SHALL terminate script execution
3. WHEN the user presses the record hotkey THEN the System SHALL toggle recording state
4. WHEN pyWinhook captures keyboard events THEN the System SHALL process the events correctly on Windows 7

# Implementation Plan

- [x] 1. Update dependency files for Windows 7 compatibility





  - [x] 1.1 Update requirements-windows.txt with PySide2 and compatible versions


    - Replace PySide6 with PySide2
    - Remove qt-material dependency
    - Update Python version comment to 3.8
    - _Requirements: 5.1, 5.3_
  - [x] 1.2 Update requirements-universal.txt with PySide2 and compatible versions


    - Replace PySide6 with PySide2
    - Remove qt-material dependency
    - _Requirements: 5.1, 5.3_

- [x] 2. Refactor main entry point (KeymouseGo.py)





  - [x] 2.1 Update PySide6 imports to PySide2


    - Change `from PySide6.QtWidgets` to `from PySide2.QtWidgets`
    - Change `from PySide6.QtCore` to `from PySide2.QtCore`
    - Update `app.exec()` to `app.exec_()`
    - _Requirements: 2.1, 2.2, 2.3, 4.1, 4.2_

- [x] 3. Refactor UI view files





  - [x] 3.1 Update UIView.py for PySide2 compatibility


    - Replace all PySide6 imports with PySide2
    - Update QIcon.Mode.Normal to QIcon.Normal
    - Update QIcon.State.Off to QIcon.Off
    - _Requirements: 7.1, 4.1, 4.2, 4.3_
  - [x] 3.2 Update UIFileDialogView.py for PySide2 compatibility


    - Replace all PySide6 imports with PySide2
    - Update QIcon enum references
    - _Requirements: 7.2, 4.1, 4.2, 4.3_

- [x] 4. Refactor UIFunc.py (main UI logic)








  - [x] 4.1 Update PySide6 imports to PySide2


    - Replace all PySide6 module imports
    - _Requirements: 2.1, 2.2, 2.3, 4.1, 4.2, 4.3_
  - [x] 4.2 Remove qt-material and implement native theme system


    - Remove `from qt_material import list_themes, QtStyleTools`
    - Remove QtStyleTools from class inheritance
    - Implement simple THEMES dictionary with Default, Dark, Light options
    - Update `onchangetheme()` method to use Qt stylesheets
    - _Requirements: 3.1, 3.2, 3.3_
  - [x] 4.3 Replace QSoundEffect with PySide2-compatible audio


    - Replace QSoundEffect with QSound from PySide2.QtMultimedia
    - Update `playtune()` method implementation
    - Remove volume slider functionality (QSound doesn't support volume)
    - _Requirements: 4.4_
  - [ ]* 4.4 Write property test for configuration round-trip
    - **Property 1: Configuration Round-Trip Consistency**
    - **Validates: Requirements 2.5**

- [x] 5. Refactor UIFileDialogFunc.py







  - [x] 5.1 Update PySide6 imports to PySide2


    - Replace all PySide6 module imports
    - _Requirements: 4.1, 4.2_


- [x] 6. Refactor Recorder module






  - [x] 6.1 Update Recorder/__init__.py for PySide2


    - Replace PySide6.QtCore import with PySide2.QtCore
    - _Requirements: 2.3, 4.2_


- [x] 7. Refactor Util module






  - [x] 7.1 Update Util/RunScriptClass.py for PySide2


    - Replace all PySide6 imports with PySide2
    - Update Signal definitions if needed
    - _Requirements: 2.2, 2.3, 4.1, 4.2, 4.5_
  - [ ]* 7.2 Write property test for UI widget interaction
    - **Property 2: UI Widget Interaction Consistency**

    - **Validates: Requirements 6.2, 6.3**

- [x] 8. Checkpoint - Ensure all tests pass







  - Ensure all tests pass, ask the user if questions arise.

- [x] 9. Update assets and resources





















  - [x] 9.1 Regenerate assets_rc.py for PySide2


    - Use pyside2-rcc to regenerate resource file
    - _Requirements: 7.3_

- [x] 10. Final verification and cleanup






  - [x] 10.1 Verify no PySide6 imports remain in codebase


    - Search all Python files for PySide6 references

    - _Requirements: 4.1, 4.2, 4.3_
  - [ ]* 10.2 Write import statement verification test
    - **Property 3: Import Statement Correctness**
    - **Validates: Requirements 2.1, 2.2, 2.3, 2.4, 4.1, 4.2, 4.3**

- [x] 11. Final Checkpoint - Ensure all tests pass






  - Ensure all tests pass, ask the user if questions arise.

- [x] 12. Build Windows 7 compatible release package






  - [x] 12.1 Install PyInstaller and build dependencies


    - Install PyInstaller compatible with Python 3.8.10
    - Ensure all runtime dependencies are installed
    - _Requirements: 1.1, 1.2, 1.3, 1.4_

  - [x] 12.2 Create PyInstaller spec file for Windows 7


    - Configure single-file executable build
    - Include assets folder (i18n, sounds)
    - Include icon file (Mondrian.ico)
    - Set Windows version info
    - _Requirements: 1.1_

  - [x] 12.3 Build the executable


    - Run PyInstaller to create Windows 7 compatible .exe
    - Verify the build completes without errors
    - _Requirements: 1.1, 1.2, 1.3, 1.4_

  - [x] 12.4 Test and package the release


    - Verify executable runs correctly
    - Create release folder with executable and necessary files
    - _Requirements: 1.1, 1.2, 1.3, 1.4_

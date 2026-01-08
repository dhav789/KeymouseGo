# Runtime hook to fix Windows 7 compatibility with pywin32
# The os.add_dll_directory function is not available on Windows 7
# This hook patches it before pywin32 tries to use it

import os
import sys

# Check if we're on Windows and if add_dll_directory is not available or broken
if sys.platform == 'win32':
    # On Windows 7, os.add_dll_directory may not exist or may fail
    # We need to patch it to prevent pywin32 bootstrap from failing
    
    _original_add_dll_directory = getattr(os, 'add_dll_directory', None)
    
    def _safe_add_dll_directory(path):
        """Safe wrapper for os.add_dll_directory that handles Windows 7"""
        try:
            if _original_add_dll_directory is not None:
                return _original_add_dll_directory(path)
        except OSError:
            # On Windows 7 or when the function fails, just ignore it
            # The DLLs should still be found via PATH
            pass
        return None
    
    os.add_dll_directory = _safe_add_dll_directory

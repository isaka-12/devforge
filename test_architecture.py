"""
Quick test script to verify the modular structure works correctly.
"""

import sys
sys.path.insert(0, 'c:/Users/user/Projects/devforge')

from devforge.scaffolders import list_available_frameworks, get_scaffolder

print("🔥 Testing DevForge Modular Architecture\n")

# Test 1: List frameworks
print("Test 1: Listing available frameworks")
frameworks = list_available_frameworks()
print(f"Available frameworks: {frameworks}")
assert len(frameworks) == 3, f"Expected 3 frameworks, got {len(frameworks)}"
print("✅ PASSED\n")

# Test 2: Get each scaffolder
print("Test 2: Getting scaffolder instances")
for fw_key in frameworks:
    scaffolder = get_scaffolder(fw_key)
    print(f"  {scaffolder.emoji} {scaffolder.framework_name} ({fw_key})")
    assert scaffolder is not None
print("✅ PASSED\n")

# Test 3: Check scaffolder properties
print("Test 3: Checking scaffolder properties")
react_scaffolder = get_scaffolder('react')
assert react_scaffolder.framework_name == "React"
assert react_scaffolder.emoji == "⚛️"
assert react_scaffolder.required_command == "npm"
print("  React scaffolder properties correct")

fastapi_scaffolder = get_scaffolder('fastapi')
assert fastapi_scaffolder.framework_name == "FastAPI"
assert fastapi_scaffolder.emoji == "🐍"
assert fastapi_scaffolder.required_command is None
print("  FastAPI scaffolder properties correct")

flutter_scaffolder = get_scaffolder('flutter')
assert flutter_scaffolder.framework_name == "Flutter"
assert flutter_scaffolder.emoji == "💙"
assert flutter_scaffolder.required_command == "flutter"
print("  Flutter scaffolder properties correct")
print("✅ PASSED\n")

print("🎉 All tests passed! Modular architecture is working correctly.")

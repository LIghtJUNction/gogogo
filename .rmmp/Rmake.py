#!/usr/bin/env python3
"""
RMM 构建脚本
自定义构建逻辑，配合 rmmproject.toml 中的构建配置使用

正确的配置说明:
[build]
prebuild = "Rmake"     # 调用下面的 prebuild() 函数进行预构建处理
build = "default"      # 使用默认构建逻辑（打包zip和tar.gz文件）
postbuild = "Rmake"    # 调用下面的 postbuild() 函数进行后构建处理

注意：
- 推荐使用上述配置，利用 Rmake.py 的 prebuild() 和 postbuild() 函数
- build() 函数被注释是因为默认构建逻辑已经足够处理大多数情况
- 如果要完全自定义构建流程，可以取消注释 build() 函数并设置 build = "Rmake"

错误配置示例（请避免）:
prebuild = "default", build = "Rmake", postbuild = "default"
"""

def prebuild():
    """预构建阶段 - 在主构建之前执行"""
    print("🔧 执行预构建逻辑...")
    print("💡 如果你想自定义预构建流程，请修改这个函数")
    
    # 示例：检查依赖
    # check_dependencies()
    
    # 示例：清理临时文件
    # cleanup_temp_files()
    
    # 示例：生成配置文件
    # generate_config_files()

def postbuild():
    """后构建阶段 - 在主构建之后执行"""
    print("🔧 执行后构建逻辑...")
    print("💡 如果你想自定义构建后的逻辑，请修改这个函数")
    
    # 示例：复制额外文件
    # copy_additional_files()
    
    # 示例：验证输出
    # validate_output()
    
    # 示例：上传到服务器
    # upload_to_server()

# def build():
#     """
#     主构建逻辑 - 如果要完全自定义构建流程，取消这个函数的注释
#     并在 rmmproject.toml 中设置 build = "Rmake"
#     """
#     print("🏗️ 执行自定义构建逻辑...")
#     
#     # 你的自定义构建代码
#     # 例如：编译代码、打包资源、生成文档等
#     
#     # 注意：如果定义了这个函数，需要自己处理输出文件的生成
#     # 输出文件应该放在 .rmmp/dist/ 目录下

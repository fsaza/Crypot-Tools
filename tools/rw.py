# -*- coding: utf-8 -*-
import os


def create_file(path, content):
    try:
        # 打开文件并写入内容,指定编码为utf-8
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"文件 '{path}' 已成功创建并写入内容。")
    except Exception as e:
        print(f"创建文件时出现错误：{e}")


def read_file(file_path):
    """
    读取文件并返回其内容。
    如果文件不存在,则抛出 FileNotFoundError。
    """
    try:
        # 解析文件路径
        normalized_path = os.path.normpath(file_path)

        # 读取文件内容
        with open(normalized_path, 'r') as file:
            content = file.read()

        return content

    except FileNotFoundError:
        # 如果文件不存在,抛出异常
        return 0


def delete_files(file_path):
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
        else:
            #无此文件
            return 0
    except (OSError, IOError) as e:
        print(f"删除文件时出现错误: {e}")
        raise e

from book import ContentType

class Model:
    def make_text_prompt(self, text: str, target_language: str) -> str:
        if target_language == '日语':
            return f"日本語に翻訳：{text}"
        else:
            return f"翻译为{target_language}：{text}"

    def make_table_prompt(self, table: str, target_language: str) -> str:
        if target_language == '日语':
            return f"日本語に翻訳、スペースと改行を保持して表を表現：\n{table}"
        else:
            return f"翻译为{target_language}，以空格和换行符表示表格：\n{table}"

    def translate_prompt(self, content, target_language: str) -> str:
        if content.content_type == ContentType.TEXT:
            return self.make_text_prompt(content.original, target_language)
        elif content.content_type == ContentType.TABLE:
            return self.make_table_prompt(content.get_original_as_str(), target_language)

    def make_request(self, prompt):
        raise NotImplementedError("子类必须实现 make_request 方法")

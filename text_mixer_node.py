class TextMixer:
    """
    Concatenate multiple text inputs into a single STRING output.
    Result = txt_1 + txt_2 + ... + txt_N
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "inputs_count_text": ("STRING", {"default": "3"}),

                "txt_1": ("STRING", {"multiline": True, "default": ""}),
                "txt_2": ("STRING", {"multiline": True, "default": ""}),
                "txt_3": ("STRING", {"multiline": True, "default": ""}),
                "txt_4": ("STRING", {"multiline": True, "default": ""}),
                "txt_5": ("STRING", {"multiline": True, "default": ""}),
                "txt_6": ("STRING", {"multiline": True, "default": ""}),
                "txt_7": ("STRING", {"multiline": True, "default": ""}),
                "txt_8": ("STRING", {"multiline": True, "default": ""}),
                "txt_9": ("STRING", {"multiline": True, "default": ""}),
                "txt_10": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "mix"
    CATEGORY = "UnaCustom"

    def _safe_int(self, s, default):
        try:
            return int(str(s).strip())
        except Exception:
            return default

    def mix(self, inputs_count_text, **kwargs):
        n = self._safe_int(inputs_count_text, 3)
        n = max(1, min(10, n))

        parts = []
        for i in range(1, n + 1):
            t = kwargs.get(f"txt_{i}", "")
            if t:
                parts.append(t)

        result = "".join(parts)
        return (result,)
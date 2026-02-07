class TextMixer:
    """
    Concatenate multiple text inputs into a single STRING output.
    Input count adjustable at runtime via the widget.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "inputs_count": ("INT", {"default": 3, "min": 1, "max": 50, "step": 1}),
                "separator": (["newline", "paragraph", "none", "space", "comma"],),
                "txt_1": ("STRING", {"default": "", "forceInput": True}),
            },
            "optional": {
                "txt_2": ("STRING", {"default": "", "forceInput": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "mix"
    CATEGORY = "UnaCustom"

    SEPARATOR_MAP = {
        "newline": "\n",
        "paragraph": "\n\n",
        "none": "",
        "space": " ",
        "comma": ", ",
    }

    def mix(self, inputs_count, separator, **kwargs):
        parts = []
        for i in range(1, inputs_count + 1):
            t = kwargs.get(f"txt_{i}", "")
            if t:
                parts.append(str(t))
        return (self.SEPARATOR_MAP[separator].join(parts),)
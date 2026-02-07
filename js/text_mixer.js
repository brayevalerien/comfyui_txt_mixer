import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "UnaCustom.TextMixer",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name !== "TextMixer") return;
        nodeType.prototype.onNodeCreated = function () {
            this._type = "STRING";
            this.addWidget("button", "Update inputs", null, () => {
                if (!this.inputs) {
                    this.inputs = [];
                }
                const target = this.widgets.find(w => w.name === "inputs_count")["value"];
                const current = this.inputs.filter(input => input.type === this._type).length;
                if (target === current) return;

                if (target < current) {
                    for (let i = 0; i < current - target; i++) {
                        this.removeInput(this.inputs.length - 1);
                    }
                } else {
                    for (let i = current + 1; i <= target; i++) {
                        this.addInput(`txt_${i}`, this._type, { shape: 7 });
                    }
                }
            });
        };
    },
});

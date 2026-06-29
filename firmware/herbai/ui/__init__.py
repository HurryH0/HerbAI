"""TFT user interface. Methods are stubbed to print() so the flow runs in a terminal;
swap the bodies for your SPI display rendering (Pillow -> framebuffer)."""


class UI:
    def splash(self, name): print(f"[UI] {name}")
    def message(self, text): print(f"[UI] {text}")
    def prompt_fill_water(self): print("[UI] Please fill water to begin.")
    def choose_crop(self):
        # TODO: render the 5-crop menu and return the tapped choice.
        return "basil"
    def dosing_guide(self, current, target, tol):
        band = "GREEN" if abs(current - target) <= tol else ("AMBER" if current < target else "RED")
        print(f"[UI] Dosing: {current} ppm -> target {target} ppm  [{band}]")
    def show_stage(self, crop, stage, day):
        print(f"[UI] {crop} · {stage.stage} · day {day} · target {stage.ppm_target} ppm")
    def nudge_add_nutrient(self, stage):
        print(f"[UI] Next stage: {stage.stage}. Add nutrient toward {stage.ppm_target} ppm.")
    def show_health(self, status): print(f"[UI] Canopy: {status}")

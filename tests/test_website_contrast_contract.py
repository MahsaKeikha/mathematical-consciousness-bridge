"""Accessibility/readability contract for the public research website."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "website" / "contrast-v2.css").read_text(encoding="utf-8")
BUILD = (ROOT / "scripts" / "prepare_website.py").read_text(encoding="utf-8")


def _rgb(hex_color: str) -> tuple[float, float, float]:
    value = hex_color.removeprefix("#")
    return tuple(int(value[i : i + 2], 16) / 255 for i in (0, 2, 4))


def _linear(channel: float) -> float:
    return channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4


def _luminance(hex_color: str) -> float:
    r, g, b = (_linear(channel) for channel in _rgb(hex_color))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _contrast(a: str, b: str) -> float:
    high, low = sorted((_luminance(a), _luminance(b)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def test_core_reading_palette_meets_normal_text_contrast() -> None:
    assert _contrast("#111827", "#ffffff") >= 7.0
    assert _contrast("#4b5563", "#ffffff") >= 4.5
    assert _contrast("#1f3a7a", "#ffffff") >= 4.5
    assert _contrast("#ffffff", "#1f3a7a") >= 4.5
    assert _contrast("#d7dde8", "#111827") >= 4.5


def test_equations_are_forced_to_dark_text_on_light_background() -> None:
    assert ".dark-section .equation" in CSS
    assert "background: #ffffff !important" in CSS
    assert "color: #111827 !important" in CSS
    assert 'mjx-container[jax="SVG"]' in CSS


def test_buttons_and_keyboard_focus_have_explicit_contrast_states() -> None:
    assert ".button.primary" in CSS
    assert "background: #1f3a7a !important" in CSS
    assert "color: #ffffff !important" in CSS
    assert "a:focus-visible" in CSS
    assert "outline: 3px solid #5272c7 !important" in CSS


def test_contrast_layer_is_injected_into_every_deployed_page() -> None:
    assert 'contrast-v2.css?v=' in BUILD
    assert '"contrast-v2.css"' in BUILD

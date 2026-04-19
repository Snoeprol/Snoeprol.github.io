#!/usr/bin/env python3
"""
Generate four GIFs for a Doppler / supersonic source post:
  1) Stationary source (standing still)
  2) Source receding from observer at v = c (Mach 1 away)
  3) Source approaching observer at v = c (Mach 1 toward)
  4) Source approaching at v = 2c (Mach 2 toward, Mach cone)

Output: ../assets/img/doppler/*.gif and arrival_wavefronts_still_vs_2c.png (run from repo root or scripts/)
"""
from __future__ import annotations

import os
import subprocess
import wave

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.colors import LinearSegmentedColormap
from pydub import AudioSegment

# Normalized sound speed (sim units = seconds, distances in plot units)
C = 1.0
OBSERVER_X = 3.2
XLIM = (-5.5, 5.5)
YLIM = (-2.6, 2.6)
FIGSIZE = (6.4, 4.0)
DPI = 100
DT_EMIT = 0.07
FPS = 24

AUDIO_FS = 44100
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Use any MP3 you like; default name lives next to this script in scripts/.
SIREN_MP3 = os.path.join(
    _SCRIPT_DIR,
    "(MP3) DRIETONIGE SIRENE NEDERLANDSE AMBULANCE.mp3",
)

# UI / theme (requested background)
BG = "#2A2D2F"
FG = "#E8EAEB"
FG_MUTED = "#9CA3AF"
EDGE = "#4B5054"
WAVE_CMAP = LinearSegmentedColormap.from_list("wave_age", ["#22D3EE", "#F97316"])


def style_axes_dark(ax) -> None:
    ax.set_facecolor(BG)
    ax.tick_params(colors=FG)
    ax.xaxis.label.set_color(FG)
    ax.yaxis.label.set_color(FG)
    for spine in ax.spines.values():
        spine.set_color(EDGE)
    t = ax.get_title()
    if t:
        ax.title.set_color(FG)


def wave_color(te: float, t_color_max: float):
    x = 0.0 if t_color_max <= 0 else min(1.0, max(0.0, te / t_color_max))
    return WAVE_CMAP(x)


def draw_wave_age_legend(
    ax, x0: float, x1: float, y: float, *, show_sublabel: bool = True
) -> None:
    """Horizontal emission-age bar with labels (uses offset points so text is not placed in data units)."""
    n = 40
    xs = np.linspace(x0, x1, n + 1)
    for i in range(n):
        frac = i / max(1, n - 1)
        ax.plot(
            [xs[i], xs[i + 1]],
            [y, y],
            color=WAVE_CMAP(frac),
            linewidth=3.0,
            solid_capstyle="round",
            zorder=9,
        )
    bar_left, bar_right = float(xs[0]), float(xs[-1])
    ax.annotate(
        "OLDER",
        xy=(bar_left, y),
        xytext=(0, 10),
        textcoords="offset points",
        ha="center",
        va="bottom",
        color="#67E8F9",
        fontsize=8,
        weight="bold",
        zorder=10,
    )
    ax.annotate(
        "NEWER",
        xy=(bar_right, y),
        xytext=(0, 10),
        textcoords="offset points",
        ha="center",
        va="bottom",
        color="#FDBA74",
        fontsize=8,
        weight="bold",
        zorder=10,
    )
    if show_sublabel:
        ax.annotate(
            "emission color",
            xy=((bar_left + bar_right) / 2, y),
            xytext=(0, -12),
            textcoords="offset points",
            ha="center",
            va="top",
            color=FG_MUTED,
            fontsize=7,
            zorder=10,
        )


def repo_root() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(here)


def out_dir() -> str:
    d = os.path.join(repo_root(), "assets", "img", "doppler")
    os.makedirs(d, exist_ok=True)
    return d


def source_x(te: float, scenario: str) -> float:
    if scenario == "still":
        return -0.5
    if scenario == "away_m1":
        # Starts near observer, moves left (away) at v = c
        return 1.4 - C * te
    if scenario == "toward_m1":
        return -4.5 + C * te
    if scenario == "toward_m2":
        return -4.5 + 2.0 * C * te
    raise ValueError(scenario)


def source_distance_zero_emit_time(scenario: str) -> float:
    return abs(OBSERVER_X - source_x(0.0, scenario))


def crossing_emit_time(scenario: str) -> float | None:
    if scenario == "toward_m1":
        return OBSERVER_X - source_x(0.0, scenario)
    if scenario == "toward_m2":
        return (OBSERVER_X - source_x(0.0, scenario)) / 2.0
    return None


def frame_times(t_max: float, dt_frame: float) -> list[float]:
    return [round(t, 5) for t in _frange(0.0, t_max, dt_frame)]


def _frange(a: float, b: float, step: float):
    t = a
    while t <= b + 1e-9:
        yield t
        t += step


def emission_times(t: float, emit_until: float | None = None) -> list[float]:
    t_end = t if emit_until is None else min(t, emit_until)
    return [round(te, 5) for te in _frange(0.0, t_end, DT_EMIT)]


def draw_frame(ax, scenario: str, t: float, emit_until: float | None = None) -> None:
    ax.clear()
    ax.set_facecolor(BG)
    ax.set_xlim(*XLIM)
    ax.set_ylim(*YLIM)
    ax.set_aspect("equal")
    ax.axis("off")

    sx_now = source_x(t, scenario)
    # Strong red/green distinction for source (ambulance) vs observer (you).
    ax.plot(
        [OBSERVER_X],
        [0.0],
        "s",
        color="#00a651",
        markeredgecolor="#86efac",
        markeredgewidth=1.2,
        markersize=10,
        label="You (green)",
        zorder=6,
    )
    ax.plot(
        [sx_now],
        [0.0],
        "o",
        color="#e11d48",
        markeredgecolor="#fca5a5",
        markeredgewidth=1.1,
        markersize=11,
        label="Ambulance (red)",
        zorder=7,
    )

    ax.text(OBSERVER_X + 0.12, 0.16, "YOU", color="#00a651", fontsize=9, weight="bold")
    ax.text(sx_now + 0.12, -0.22, "AMB", color="#e11d48", fontsize=9, weight="bold")

    emitted = emission_times(t, emit_until)
    t_color_max = max(emitted[-1], DT_EMIT) if emitted else DT_EMIT
    for te in emitted:
        r = C * (t - te)
        if r <= 0:
            continue
        x0, y0 = source_x(te, scenario), 0.0
        color = wave_color(te, t_color_max)
        circ = plt.Circle(
            (x0, y0),
            r,
            fill=False,
            edgecolor=color,
            linewidth=1.15,
            alpha=0.7,
            zorder=1,
        )
        ax.add_patch(circ)

    if emitted:
        ax.text(
            XLIM[0] + 0.25,
            YLIM[0] + 0.2,
            "Wave color = emission age",
            color=FG_MUTED,
            fontsize=8,
            bbox={"facecolor": "#333637", "edgecolor": EDGE, "pad": 3},
        )
        draw_wave_age_legend(ax, XLIM[0] + 0.35, XLIM[0] + 2.6, YLIM[0] + 0.58)

    leg = ax.legend(
        loc="upper right",
        frameon=True,
        fontsize=9,
        facecolor=BG,
        edgecolor=EDGE,
        labelcolor=FG,
    )
    for text in leg.get_texts():
        text.set_color(FG)


def make_gif(
    filename: str,
    scenario: str,
    title: str,
    t_max: float,
    dt_frame: float,
    emit_until: float | None = None,
) -> str:
    path = os.path.join(out_dir(), filename)
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    times = frame_times(t_max, dt_frame)

    def _update(ti: int):
        t = times[ti]
        draw_frame(ax, scenario, t, emit_until)
        ax.set_title(title, fontsize=12, pad=10, color=FG)
        if emit_until is not None and t > emit_until:
            ax.text(
                XLIM[0] + 0.25,
                YLIM[1] - 0.35,
                "Siren OFF - old wavefronts keep propagating",
                color="#fecaca",
                fontsize=9,
                weight="bold",
                bbox={"facecolor": "#3f2426", "edgecolor": "#7f1d1d", "pad": 4},
            )

    anim = animation.FuncAnimation(
        fig,
        _update,
        frames=len(times),
        interval=1000 / FPS,
        blit=False,
    )
    writer = animation.PillowWriter(fps=FPS)
    anim.save(path, writer=writer)
    plt.close(fig)
    return path


# -----------------------------
# Audio generation (Doppler-correct)
# -----------------------------
def load_siren() -> tuple[np.ndarray, int]:
    seg = AudioSegment.from_file(SIREN_MP3).set_channels(1).set_frame_rate(AUDIO_FS)
    samples = np.array(seg.get_array_of_samples()).astype(np.float32)
    peak = float(np.max(np.abs(samples))) or 1.0
    return samples / peak, AUDIO_FS


def _interp_source(source: np.ndarray, t_e: np.ndarray) -> np.ndarray:
    valid = (t_e >= 0) & (t_e <= (len(source) - 2) / AUDIO_FS) & ~np.isnan(t_e)
    idx_f = np.where(valid, t_e * AUDIO_FS, 0.0)
    i0 = idx_f.astype(np.int64)
    frac = idx_f - i0
    out = (1.0 - frac) * source[i0] + frac * source[np.minimum(i0 + 1, len(source) - 1)]
    return np.where(valid, out, 0.0).astype(np.float32)


def _t_e_branches(
    scenario: str, t_obs: np.ndarray, emit_until: float | None
) -> list[np.ndarray]:
    """Return list of t_e arrays (one per branch). Invalid samples set to NaN."""
    nan = np.full_like(t_obs, np.nan, dtype=np.float64)
    emit_max = emit_until if emit_until is not None else 1e9
    cross = crossing_emit_time(scenario)

    if scenario == "still":
        d = source_distance_zero_emit_time(scenario)
        t_e = t_obs - d / C
        t_e = np.where((t_e >= 0) & (t_e <= emit_max), t_e, np.nan)
        return [t_e]

    if scenario == "away_m1":
        d0 = source_distance_zero_emit_time(scenario)
        t_e = (t_obs - d0 / C) / 2.0
        t_e = np.where((t_e >= 0) & (t_e <= emit_max), t_e, np.nan)
        return [t_e]

    if scenario == "toward_m1":
        d0 = source_distance_zero_emit_time(scenario)
        pre = nan.copy()
        post = nan.copy()
        if cross is not None:
            t_arrive_pre = d0 / C
            post_t_e = (t_obs + d0 / C) / 2.0
            valid_post = (t_obs >= t_arrive_pre) & (post_t_e >= cross) & (post_t_e <= emit_max)
            post = np.where(valid_post, post_t_e, np.nan)
        return [pre, post]

    if scenario == "toward_m2":
        d0 = source_distance_zero_emit_time(scenario)
        t_arrive_shock = d0 / C - cross
        pre_t_e = d0 / C - t_obs
        valid_pre = (t_obs >= t_arrive_shock) & (pre_t_e >= 0) & (pre_t_e <= min(cross, emit_max))
        pre = np.where(valid_pre, pre_t_e, np.nan)
        post_t_e = (t_obs + d0 / C) / 3.0
        valid_post = (post_t_e >= cross) & (post_t_e <= emit_max)
        post = np.where(valid_post, post_t_e, np.nan)
        return [pre, post]

    return [nan]


def generate_audio(
    scenario: str, sim_duration: float, emit_until: float | None, source: np.ndarray
) -> np.ndarray:
    n_out = int(sim_duration * AUDIO_FS)
    t_obs = np.arange(n_out) / AUDIO_FS
    out = np.zeros(n_out, dtype=np.float32)
    for t_e in _t_e_branches(scenario, t_obs, emit_until):
        out += _interp_source(source, t_e)

    if scenario == "toward_m1":
        # Degenerate stack-up: all pre-crossing emissions arrive simultaneously
        # at t_obs = d0/c. Synthesize an envelope-modulated burst from that audio.
        d0 = source_distance_zero_emit_time(scenario)
        cross = crossing_emit_time(scenario)
        emit_end = emit_until if emit_until is not None else cross
        n_emit = int(min(emit_end, cross) * AUDIO_FS)
        if n_emit > 1:
            burst_n = int(0.18 * AUDIO_FS)
            xp = np.linspace(0, n_emit - 1, burst_n)
            burst = np.interp(xp, np.arange(n_emit), source[:n_emit]).astype(np.float32)
            window = np.hanning(burst_n).astype(np.float32)
            burst *= window * 1.6
            center = int(d0 / C * AUDIO_FS)
            start = max(0, center - burst_n // 2)
            end = min(n_out, start + burst_n)
            out[start:end] += burst[: end - start]

    peak = float(np.max(np.abs(out))) or 1.0
    return (out / peak * 0.95).astype(np.float32)


def write_wav(path: str, samples: np.ndarray, fs: int) -> None:
    s16 = np.clip(samples * 32767.0, -32768, 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(fs)
        w.writeframes(s16.tobytes())


def make_video_with_audio(
    filename: str,
    scenario: str,
    title: str,
    t_max: float,
    dt_frame: float,
    emit_until: float | None,
    source: np.ndarray,
) -> str:
    path = os.path.join(out_dir(), filename)
    silent_mp4 = path.replace(".mp4", "_silent.mp4")
    wav_path = path.replace(".mp4", ".wav")

    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    times = frame_times(t_max, dt_frame)
    arrival_indicator = {"hit_count": 0}

    def _update(ti: int):
        t = times[ti]
        draw_frame(ax, scenario, t, emit_until)
        ax.set_title(title, fontsize=12, pad=10, color=FG)

        if emit_until is not None and t > emit_until:
            ax.text(
                XLIM[0] + 0.25,
                YLIM[1] - 0.35,
                "Siren OFF - old wavefronts keep propagating",
                color="#fecaca",
                fontsize=9,
                weight="bold",
                bbox={"facecolor": "#3f2426", "edgecolor": "#7f1d1d", "pad": 4},
            )

        # Highlight observer when audio is currently arriving (t_e valid in any branch)
        any_audio = False
        t_e_branches = _t_e_branches(scenario, np.array([t]), emit_until)
        for arr in t_e_branches:
            if not np.all(np.isnan(arr)):
                any_audio = True
                break
        if scenario == "toward_m1":
            burst_t = source_distance_zero_emit_time(scenario) / C
            if abs(t - burst_t) < 0.18:
                any_audio = True
        if any_audio:
            arrival_indicator["hit_count"] += 1
            ax.plot(
                [OBSERVER_X],
                [0.0],
                "o",
                markerfacecolor="none",
                markeredgecolor="#FACC15",
                markeredgewidth=2.0,
                markersize=22,
                zorder=5,
            )
            ax.text(
                OBSERVER_X - 0.6,
                0.55,
                "HEARING",
                color="#FACC15",
                fontsize=9,
                weight="bold",
            )

    anim = animation.FuncAnimation(
        fig, _update, frames=len(times), interval=1000 / FPS, blit=False
    )
    writer = animation.FFMpegWriter(fps=FPS, codec="libx264", bitrate=2400)
    anim.save(silent_mp4, writer=writer, savefig_kwargs={"facecolor": BG})
    plt.close(fig)

    audio = generate_audio(scenario, t_max, emit_until, source)
    write_wav(wav_path, audio, AUDIO_FS)

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-loglevel",
            "error",
            "-i",
            silent_mp4,
            "-i",
            wav_path,
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "160k",
            "-shortest",
            path,
        ],
        check=True,
    )

    try:
        os.remove(silent_mp4)
        os.remove(wav_path)
    except OSError:
        pass
    return path


def make_arrival_wavefronts_summary(
    filename: str,
    emit_until: float,
    scenarios: list[tuple[str, str]],
    suptitle: str = "Observed colored wave arrivals (vertical lines) by scenario",
) -> str:
    """
    Build stacked arrival-wave plots (vertical colored lines).
    Line color encodes emission age: OLDER -> NEWER.
    """
    path = os.path.join(out_dir(), filename)

    t_emit = np.arange(0.0, emit_until + 1e-9, DT_EMIT)
    t_color_max = max(float(t_emit[-1]), DT_EMIT)
    emitted_colors = [wave_color(float(te), t_color_max) for te in t_emit]

    fig_h = 5.0 if len(scenarios) <= 2 else 7.0
    fig, axes = plt.subplots(
        len(scenarios),
        1,
        figsize=(8.0, fig_h),
        dpi=DPI,
        constrained_layout=False,
        sharex=False,
    )
    if len(scenarios) == 1:
        axes = [axes]
    fig.patch.set_facecolor(BG)
    # Room above panels for title + color note; room below for bottom captions.
    fig.subplots_adjust(left=0.11, right=0.97, top=0.82, bottom=0.10, hspace=0.42)
    fig.suptitle(suptitle, fontsize=12, color=FG, y=0.97)
    fig.text(
        0.5,
        0.905,
        "Color scale (all panels): cyan = older emission → orange = newer emission",
        ha="center",
        va="top",
        fontsize=8,
        color=FG_MUTED,
    )

    # Vertical bands (axis coords): keep data in the middle; labels live in margins.
    y_v0, y_v1 = 0.18, 0.62
    y_emit = 0.74

    for ax, (scenario, label) in zip(axes, scenarios):
        style_axes_dark(ax)
        ax.set_ylim(0.0, 1.0)
        ax.set_yticks([])
        ax.set_ylabel(label, color=FG, fontsize=9)

        x_emit = np.array([source_x(float(te), scenario) for te in t_emit])
        t_arrival = t_emit + np.abs(OBSERVER_X - x_emit) / C
        order = np.argsort(t_arrival)
        t_arr_sorted = t_arrival[order]
        emit_sorted = t_emit[order]
        colors_sorted = [wave_color(float(te), t_color_max) for te in emit_sorted]

        # Vertical "wavefronts" arriving at observer
        ax.vlines(t_arr_sorted, y_v0, y_v1, colors=colors_sorted, linewidth=2.2, alpha=0.95)

        # Reference strip for emitted order (always OLDER -> NEWER)
        x0 = float(np.min(t_arr_sorted))
        x1 = float(np.max(t_arr_sorted))
        if x1 - x0 < 1e-6:
            x1 = x0 + 1.0
        xs = np.linspace(x0, x1, len(t_emit))
        ax.scatter(xs, np.full_like(xs, y_emit), c=emitted_colors, s=22, marker="s", zorder=5)

        ax.text(
            0.5,
            0.895,
            "emitted order (older → newer)",
            transform=ax.transAxes,
            ha="center",
            va="bottom",
            fontsize=8,
            color=FG_MUTED,
            clip_on=False,
        )
        # Inside axes (above x-ticks): negative transAxes overlaps tick labels.
        ax.text(
            0.5,
            0.098,
            "observed arrivals",
            transform=ax.transAxes,
            ha="center",
            va="bottom",
            fontsize=8,
            color=FG_MUTED,
            clip_on=False,
            zorder=6,
        )

        # Arrival order vs emission index order (order = argsort by arrival time).
        reversed_count = int(np.sum(np.diff(order) < 0))
        if reversed_count > 0:
            msg = f"reordering visible ({reversed_count} inversions)"
            msg_color = "#FCA5A5"
            box_face = "#3f2426"
            box_edge = "#7f1d1d"
        else:
            msg = "order preserved (no reversal)"
            msg_color = "#86EFAC"
            box_face = "#203428"
            box_edge = "#14532d"
        ax.text(
            0.99,
            0.95,
            msg,
            transform=ax.transAxes,
            ha="right",
            va="top",
            color=msg_color,
            fontsize=8,
            bbox={"facecolor": box_face, "edgecolor": box_edge, "pad": 3},
        )

        ax.grid(alpha=0.2, color=EDGE, axis="x")

    axes[-1].set_xlabel("Observer time", color=FG)

    fig.savefig(path)
    plt.close(fig)
    return path


def main() -> int:
    # (filename, scenario, title, sim_duration, dt_frame, emit_until)
    specs = [
        (
            "standing_still",
            "still",
            "Standing still — source not moving (circular wavefronts)",
            8.0,
            1.0 / FPS,
            None,
        ),
        (
            "away_mach1",
            "away_m1",
            "Moving away at the speed of sound (v = c) — pitch drops to half",
            8.0,
            1.0 / FPS,
            None,
        ),
        (
            "toward_mach1",
            "toward_m1",
            "Toward you at the speed of sound (v = c) — sonic pile-up burst",
            8.5,
            1.0 / FPS,
            None,
        ),
        (
            "toward_mach2",
            "toward_m2",
            "Toward you at v = 2c — siren turns off; you hear it REVERSED",
            8.5,
            1.0 / FPS,
            2.5,
        ),
    ]

    source, _ = load_siren()
    written: list[str] = []

    for fname, scen, ttl, tmax, dt, emit_until in specs:
        gif_path = make_gif(f"{fname}.gif", scen, ttl, tmax, dt, emit_until=emit_until)
        written.append(gif_path)
        print(gif_path)
        mp4_path = make_video_with_audio(
            f"{fname}.mp4", scen, ttl, tmax, dt, emit_until, source
        )
        written.append(mp4_path)
        print(mp4_path)

    arrival_summary_path = make_arrival_wavefronts_summary(
        filename="arrival_wavefronts_still_vs_2c.png",
        emit_until=2.5,
        scenarios=[
            ("still", "Standing still (v = 0)"),
            ("toward_m2", "Toward at v = 2c"),
        ],
        suptitle="Standing still vs moving at 2c: observed colored arrivals",
    )
    print(arrival_summary_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

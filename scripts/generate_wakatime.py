#!/usr/bin/env python3
"""
Generate a real-time WakaTime Stats SVG card matching the compact midnight-purple theme.
"""

import os
import sys
import json
import ssl
import urllib.request

# Fallback language color palette (GitHub Linguist standard colors)
DEFAULT_LANG_COLORS = {
    "Python": "#3572A5",
    "JavaScript": "#f1e05a",
    "TypeScript": "#3178c6",
    "Markdown": "#083fa1",
    "HTML": "#e34c26",
    "CSS": "#663399",
    "Bash": "#89e051",
    "Shell": "#89e051",
    "JSON": "#292929",
    "YAML": "#cb171e",
    "Go": "#00ADD8",
    "Text": "#858585",
    "RobotFramework": "#00c0b5",
    "Git Config": "#F44D27",
    "XML": "#0060ac",
    "Docker": "#384d54",
    "Dart": "#00B4AB",
    "Nunjucks": "#3d8137",
    "TSConfig": "#3178c6",
    "C++": "#f34b7d",
    "C": "#555555",
    "INI": "#d1dbe0",
    "CSV": "#237346",
    "Java": "#b07219",
    "Git": "#F05032",
    "SQL": "#e38c00",
    "Prisma": "#0c344b",
    "SCSS": "#c6538c",
    "TOML": "#9c4221",
    "Jinja2": "#b41717",
    "Jinja": "#b41717",
    "PowerShell": "#012456",
    "Rust": "#dea584",
    "Swift": "#F05138",
    "Solidity": "#AA6746",
    "GraphQL": "#e10098",
    "Svelte": "#ff3e00",
    "Twig": "#c1d026",
    "Makefile": "#427819",
    "Astro": "#ff5a03",
    "EJS": "#a91e50",
    "JSX": "#61dafb",
    "Other": "#858585"
}

def get_language_colors():
    """Attempt to fetch latest language colors dynamically, or use fallback."""
    colors = dict(DEFAULT_LANG_COLORS)
    try:
        ctx = ssl._create_unverified_context()
        url = "https://raw.githubusercontent.com/anuraghazra/github-readme-stats/master/src/common/languageColors.json"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5, context=ctx) as resp:
            remote_colors = json.loads(resp.read().decode("utf-8"))
            for k, v in remote_colors.items():
                if v:
                    colors[k] = v
    except Exception as e:
        print(f"Notice: Using bundled language color map ({e})", file=sys.stderr)
    return colors

def fetch_wakatime_stats(api_key, time_range="all_time"):
    """Fetch user stats from WakaTime API."""
    ctx = ssl._create_unverified_context()
    url = f"https://wakatime.com/api/v1/users/current/stats/{time_range}?api_key={api_key}"
    req = urllib.request.Request(url, headers={"User-Agent": "WakaTime-SVG-Generator/1.0"})
    with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        if "data" not in data:
            raise ValueError(f"Unexpected WakaTime API response: {data}")
        return data["data"]

def format_time_text(lang):
    """Format time string like '1,250 hrs 36 mins', '52 hrs 9 mins', '49 mins'."""
    hours = lang.get("hours", 0)
    minutes = lang.get("minutes", 0)
    
    parts = []
    if hours > 0:
        parts.append(f"{hours:,} {'hr' if hours == 1 else 'hrs'}")
    if minutes > 0:
        parts.append(f"{minutes} {'min' if minutes == 1 else 'mins'}")
        
    if not parts:
        return "0 mins"
    return " ".join(parts)

def generate_svg(stats, lang_colors, max_languages=60, title="WakaTime Stats", bg_color="#000000"):
    """Generate exact compact layout WakaTime SVG matching the midnight-purple theme."""
    raw_languages = stats.get("languages", [])
    
    # Filter languages with actual coding time
    languages = [
        l for l in raw_languages 
        if l.get("hours", 0) > 0 or l.get("minutes", 0) > 0 or l.get("total_seconds", 0) >= 60
    ][:max_languages]
    
    if not languages:
        languages = [{"name": "No activity", "percent": 100, "text": "0 mins", "hours": 0, "minutes": 0}]

    # Recalculate percentages so the progress bar sums to 100%
    total_pct = sum(l.get("percent", 0) for l in languages)
    if total_pct > 0:
        scale = 100.0 / total_pct
        for l in languages:
            l["calc_percent"] = l.get("percent", 0) * scale
    else:
        for l in languages:
            l["calc_percent"] = 100.0 / len(languages)

    # Layout constants matching github-readme-stats compact layout
    card_width = 495
    line_height = 25
    progress_bar_x = 25
    progress_bar_width = card_width - (progress_bar_x * 2)  # 445px
    progress_bar_height = 8

    # Calculate card height dynamically based on number of rows (2 items per row)
    rows_count = (len(languages) + 1) // 2
    card_height = 90 + rows_count * line_height

    # Generate progress bar rects
    progress_rects = []
    current_x = progress_bar_x
    for l in languages:
        lang_name = l.get("name", "Other")
        color = lang_colors.get(lang_name, "#858585")
        segment_width = (progress_bar_width * l["calc_percent"]) / 100.0
        progress_rects.append(
            f'    <rect mask="url(#rect-mask)" data-testid="lang-progress" x="{current_x:.2f}" y="0" width="{segment_width:.2f}" height="{progress_bar_height}" fill="{color}" />'
        )
        current_x += segment_width

    # Generate 2-column language items
    left_x = 25
    right_x = 230
    lang_items = []
    
    for idx, l in enumerate(languages):
        lang_name = l.get("name", "Other")
        color = lang_colors.get(lang_name, "#858585")
        time_text = format_time_text(l)
        
        is_left = (idx % 2 == 0)
        col_x = left_x if is_left else right_x
        row_idx = idx // 2
        item_y = 25 + (row_idx * line_height)
        
        # Escape any special XML characters in language names
        safe_name = lang_name.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        
        item_svg = f'''    <g transform="translate({col_x}, {item_y})">
      <circle cx="5" cy="6" r="5" fill="{color}" />
      <text data-testid="lang-name" x="15" y="10" class="lang-name">
        {safe_name} - {time_text}
      </text>
    </g>'''
        lang_items.append(item_svg)

    svg_content = f'''<svg
  width="{card_width}"
  height="{card_height}"
  viewBox="0 0 {card_width} {card_height}"
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
  role="img"
  aria-label="{title}"
>
  <title id="titleId">{title}</title>
  <style>
    .header {{
      font: 700 18px 'Segoe UI', Ubuntu, -apple-system, BlinkMacSystemFont, Sans-Serif;
      fill: #9745f5;
      animation: fadeInAnimation 0.8s ease-in-out forwards;
    }}
    .lang-name {{
      font: 400 11px 'Segoe UI', Ubuntu, -apple-system, BlinkMacSystemFont, Sans-Serif;
      fill: #ffffff;
    }}
    @keyframes fadeInAnimation {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}
    #rect-mask rect {{
      animation: slideInAnimation 1s ease-in-out forwards;
    }}
    @keyframes slideInAnimation {{
      from {{ width: 0; }}
      to {{ width: {progress_bar_width}px; }}
    }}
  </style>

  <!-- Background (pitch black matching midnight-purple theme) -->
  <rect
    data-testid="card-bg"
    x="0.5"
    y="0.5"
    rx="6"
    height="{card_height - 1}"
    width="{card_width - 1}"
    fill="{bg_color}"
    stroke="{bg_color}"
  />

  <!-- Card Title -->
  <g data-testid="card-title" transform="translate(25, 35)">
    <text x="0" y="0" class="header" data-testid="header">{title}</text>
  </g>

  <!-- Main Card Body -->
  <g data-testid="main-card-body" transform="translate(0, 55)">
    <!-- Progress Bar Mask with Rounded Corners -->
    <mask id="rect-mask">
      <rect x="{progress_bar_x}" y="0" width="{progress_bar_width}" height="{progress_bar_height}" fill="white" rx="4" />
    </mask>

    <!-- Language Progress Segments -->
{chr(10).join(progress_rects)}

    <!-- 2-Column Language List -->
{chr(10).join(lang_items)}
  </g>
</svg>
'''
    return svg_content

def main():
    api_key = os.environ.get("WAKATIME_API_KEY", "").strip()
    if not api_key:
        if len(sys.argv) > 1:
            api_key = sys.argv[1].strip()
        else:
            print("Error: WAKATIME_API_KEY environment variable not set.", file=sys.stderr)
            sys.exit(1)

    time_range = os.environ.get("WAKATIME_RANGE", "all_time")
    output_path = os.environ.get("OUTPUT_PATH", "assets/wakatime.svg")
    title = os.environ.get("CARD_TITLE", "WakaTime Stats")
    bg_color = os.environ.get("BG_COLOR", "#000000")

    print(f"Fetching WakaTime stats (range: {time_range})...")
    stats = fetch_wakatime_stats(api_key, time_range=time_range)

    print("Loading language colors...")
    colors = get_language_colors()

    print("Generating SVG card...")
    svg = generate_svg(stats, colors, title=title, bg_color=bg_color)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"Successfully generated {output_path} ({len(svg)} bytes)")

if __name__ == "__main__":
    main()

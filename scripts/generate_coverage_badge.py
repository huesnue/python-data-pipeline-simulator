import xml.etree.ElementTree as ET

def read_coverage_percentage(xml_path: str) -> float:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    line_rate = float(root.attrib["line-rate"])
    return round(line_rate * 100, 2)

def generate_badge_svg(percentage: float) -> str:
    color = "red"
    if percentage >= 90:
        color = "brightgreen"
    elif percentage >= 75:
        color = "green"
    elif percentage >= 60:
        color = "yellow"
    elif percentage >= 40:
        color = "orange"

    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="150" height="20">
  <linearGradient id="smooth" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <rect rx="3" width="150" height="20" fill="#555"/>
  <rect rx="3" x="70" width="80" height="20" fill="{color}"/>
  <path fill="{color}" d="M70 0h4v20h-4z"/>
  <rect rx="3" width="150" height="20" fill="url(#smooth)"/>
  <g fill="#fff" text-anchor="middle"
     font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
    <text x="35" y="14">coverage</text>
    <text x="110" y="14">{percentage}%</text>
  </g>
</svg>
""".strip()

def main():
    coverage = read_coverage_percentage("coverage.xml")
    svg = generate_badge_svg(coverage)
    with open("coverage-badge.svg", "w") as f:
        f.write(svg)
    print(f"Generated badge with {coverage}% coverage")

if __name__ == "__main__":
    main()

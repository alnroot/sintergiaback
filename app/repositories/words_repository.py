import requests


INITIAL_WORDS = [
    "Momentum", "Volatility", "Trend", "Liquidity", "Volume",
    "Resistance", "Support", "Breakout", "Pullback", "Accumulation",
    "Viral", "Meme", "Trending", "Engagement", "Amplification",
    "Resonance", "Propagation", "Adoption", "Virality", "Diffusion",
    "Sentiment", "Consensus", "FOMO", "FUD", "Hype",
    "Fear Index", "Greed Index", "Social Volume", "Crowd Wisdom", "Mass Psychology",
    "Cycles", "Fractals", "Wavelets", "Correlation", "Synchronicity",
    "Time Frame", "Momentum Wave", "Price Pattern", "Market Pulse", "Trading Wave",
    "Coherence", "Alignment", "Social Field", "Egregore", "Thoughtform",
    "Morphic Field", "Network Effect", "Crowd Mind", "Collective Intent", "Swarm Intelligence",
    "Engagement Rate", "Viral Coefficient", "Network Density", "Adoption Curve", "Growth Rate",
    "Retention", "Stickiness", "Social Proof", "Critical Mass", "Tipping Point",
    "Convergence", "Catalysis", "Breakthrough", "Flash Point", "Singularity",
    "Perfect Storm", "Alignment", "Confluence", "Synchronicity", "Resonance Point",
    "Mass Flow", "Group Think", "Hive Mind", "Collective Flow", "Social Coherence",
    "Market Sentiment", "Crowd Wisdom", "Swarm Behavior", "Emergent Order", "Social Proof",
    "Energy Flow", "Vibe Check", "Resonance", "Harmonic", "Frequency",
    "Wave Pattern", "Pulse", "Rhythm", "Oscillation", "Vibration",
    "⚡️", "↗️", "↘️", "⭐️", "🌊", "🔄", "📈", "📉", "💫", "🌀",
    "∞", "⚛", "✧", "◈", "⟡", "☯", "⚕", "φ", "π", "Ω"
]

class WordsExporter:
    def __init__(self, service_url=None):
        self.service_url = service_url

    def fetch_words(self):
        if self.service_url:
            response = requests.get(self.service_url)
            if response.status_code == 200:
                return response.json().get('words', [])
            else:
                response.raise_for_status()
        else:
            return INITIAL_WORDS

    def export_words(self, words):
        with open('exported_words.txt', 'w') as file:
            for word in words:
                file.write(f"{word}\n")

    def export_initial_words(self):
        words = self.fetch_words()
        # self.export_words(words)

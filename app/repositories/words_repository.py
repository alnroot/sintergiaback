import requests


INITIAL_WORDS = [
    "BTC102K", "CryptoRally", "BTCBreakout", "AllTimeHigh", "BTCBull",
    "NewATH", "CryptoWealth", "DigitalGold", "BTCSeason", "MassAdoption",
        "XRPBull", "RippleRally", "XRPReserve", "GarlinghouseEffect", "RippleWave",
    "XRPMomentum", "RippleBreakout", "XRPSurge", "CryptoRegulation", "InstituionalXRP",
    
    "TrillionCap", "CryptoTrillion", "StablecoinFlow", "MarketVolume", "BullMarket",
    "InstitutionalFlow", "ETFDemand", "CryptoETF", "InvestorConfidence", "MarketMomentum",
    
    "RetailStrength", "JobMarket", "EconomicResilience", "FedPolicy", "InflationWatch",
    "ConsumerSpending", "MarketPulse", "EconomicData", "MarketSentiment", "FedWatch",
    
    "Breakthrough", "Consolidation", "ResistanceBreak", "SupportLevel", "TechnicalBreakout",
    "PriceDiscovery", "MarketStructure", "TrendLine", "VolumeProfile", "PriceMomentum",
    
    "CryptoSentiment", "MarketOptimism", "BullishConsensus", "InvestorMood", "MarketPsychology",
    "SocialVolume", "CryptoTrend", "MarketNarrative", "InvestorConfidence", "CommunityMood",
    
    "InstitutionalBuying", "CorporateAdoption", "ETFInflow", "WallStreetCrypto", "MainstreamCrypto",
    "InstitutionalDemand", "CryptoIntegration", "FinancialInnovation", "CryptoRegulation", "MarketMaturity",
    
    "LiquidityFlow", "MarketDepth", "OrderFlow", "TradingVolume", "PriceAction",
    "MarketEfficiency", "TradingActivity", "MarketLiquidity", "VolumeSurge", "PriceDiscovery",
    
    "⚡️", "↗️", "🚀", "💹", "📈",
    "🌕", "💎", "🔥", "⭐️", "💫",
    
    "∞", "↗", "⚛", "◈", "⟡",
    "₿", "✧", "◊", "∆", "Ω",
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

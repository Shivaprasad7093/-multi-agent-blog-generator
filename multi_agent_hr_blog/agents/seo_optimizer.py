class SEOOptimizer:
    def optimize_content(self, content):
        # Basic SEO improvements (adding keywords, headings)
        optimized_content = content.replace("AI", "Artificial Intelligence (AI)")
        optimized_content = optimized_content.replace("HR", "Human Resources (HR)")
        return optimized_content

if __name__ == "__main__":
    seo = SEOOptimizer()
    sample_content = "AI is changing HR."
    print(seo.optimize_content(sample_content))

from agents.research_agent import ResearchAgent
from agents.content_planner import ContentPlanner
from agents.content_generator import ContentGenerator
from agents.seo_optimizer import SEOOptimizer
from agents.review_agent import ReviewAgent

def main():
    research_agent = ResearchAgent()
    topics = research_agent.fetch_trending_topics()
    print("Trending Topics:", topics)

    content_planner = ContentPlanner()
    outline = content_planner.generate_outline(topics[0])

    content_generator = ContentGenerator()
    blog_content = content_generator.generate_blog(outline)

    seo_optimizer = SEOOptimizer()
    seo_content = seo_optimizer.optimize_content(blog_content)

    review_agent = ReviewAgent()
    final_blog = review_agent.review_content(seo_content)

    with open("final_blog.md", "w") as f:
        f.write(final_blog)

    print("Blog post generated and saved as final_blog.md")

if __name__ == "__main__":
    main()

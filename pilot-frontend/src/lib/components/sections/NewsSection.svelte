<script>
  import { getImageUrl } from '$lib/utils/image.js';

  let { data } = $props();
</script>

<section class="news-section">
  <div class="container">
    {#if data.section_title}
      <h2 class="section-title">{data.section_title}</h2>
    {/if}

    <div class="news-grid">
      {#each data.news_items as item}
        <article class="news-item">
          {#if item.image}
            <div class="news-image">
              <img src={getImageUrl(item.image.url)} alt={item.image.title} />
            </div>
          {/if}
          <div class="news-content">
            {#if item.date}
              <time class="news-date">{new Date(item.date).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}</time>
            {/if}
            {#if item.category}
              <span class="news-category">{item.category}</span>
            {/if}
            <h3 class="news-title">{item.title}</h3>
            {#if item.summary}
              <div class="news-summary">
                {@html item.summary}
              </div>
            {/if}
            {#if item.link_url}
              <a href={item.link_url} class="news-link">
                {item.link_text || 'Read More'} →
              </a>
            {/if}
          </div>
        </article>
      {/each}
    </div>
  </div>
</section>

<style>
  .news-section {
    padding: 60px 20px;
    background: #f8f9fa;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
  }

  .section-title {
    text-align: center;
    font-size: 2.5rem;
    color: #1a1a1a;
    margin-bottom: 40px;
  }

  .news-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 30px;
  }

  .news-item {
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }

  .news-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
  }

  .news-image {
    width: 100%;
    height: 200px;
    overflow: hidden;
    background: #e0e0e0;
  }

  .news-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .news-content {
    padding: 25px;
  }

  .news-date {
    display: block;
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 10px;
  }

  .news-category {
    display: inline-block;
    padding: 4px 10px;
    background: #0066cc;
    color: white;
    font-size: 0.75rem;
    border-radius: 12px;
    font-weight: 500;
    margin-bottom: 10px;
  }

  .news-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: #1a1a1a;
    margin-bottom: 15px;
    line-height: 1.4;
  }

  .news-summary {
    font-size: 1rem;
    color: #555;
    line-height: 1.6;
    margin-bottom: 15px;
  }

  .news-summary :global(p) {
    margin-bottom: 10px;
  }

  .news-summary :global(a) {
    color: #0066cc;
    text-decoration: underline;
  }

  .news-link {
    display: inline-block;
    color: #0066cc;
    font-weight: 500;
    text-decoration: none;
    transition: transform 0.2s ease;
  }

  .news-link:hover {
    transform: translateX(3px);
    text-decoration: underline;
  }

  @media (max-width: 768px) {
    .section-title {
      font-size: 2rem;
    }

    .news-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

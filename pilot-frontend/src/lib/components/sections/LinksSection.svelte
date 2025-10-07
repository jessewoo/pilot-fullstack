<script>
  let { data } = $props();
</script>

<section class="links-section">
  <div class="container">
    <div class="links-grid">
      {#each data.links as link}
        <a href={link.url} class="link-card">
          {#if link.icon}
            <div class="link-icon">{link.icon}</div>
          {/if}
          <h3 class="link-title">{link.title}</h3>
          {#if link.description}
            <p class="link-description">{link.description}</p>
          {/if}
          <span class="link-arrow">→</span>
        </a>
      {/each}
    </div>
  </div>
</section>

<style>
  .links-section {
    padding: 30px 20px;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
  }

  .links-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
  }

  .link-card {
    display: block;
    background: #f8f9fa;
    padding: 30px;
    border-radius: 8px;
    border: 2px solid transparent;
    text-decoration: none;
    color: inherit;
    transition: all 0.2s ease;
    position: relative;
  }

  .link-card:hover {
    border-color: #0066cc;
    transform: translateY(-3px);
    box-shadow: 0 4px 12px rgba(0,102,204,0.2);
    text-decoration: none;
  }

  .link-icon {
    font-size: 2rem;
    margin-bottom: 15px;
  }

  .link-title {
    font-size: 1.5rem;
    color: #1a1a1a;
    margin-bottom: 10px;
    font-weight: 600;
  }

  .link-description {
    font-size: 1rem;
    color: #666;
    line-height: 1.6;
    margin-bottom: 15px;
  }

  .link-arrow {
    position: absolute;
    bottom: 20px;
    right: 30px;
    font-size: 1.5rem;
    color: #0066cc;
    transition: transform 0.2s ease;
  }

  .link-card:hover .link-arrow {
    transform: translateX(5px);
  }

  @media (max-width: 768px) {
    .section-title {
      font-size: 2rem;
    }

    .links-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

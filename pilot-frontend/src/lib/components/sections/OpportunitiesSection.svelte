<script>
  let { data } = $props();
</script>

<section class="opportunities-section">
  <div class="container">
    {#if data.section_title}
      <h2 class="section-title">{data.section_title}</h2>
    {/if}

    <div class="opportunities-grid">
      {#each data.opportunities as opportunity}
        <div class="opportunity-card">
          {#if opportunity.badge}
            <span class="badge">{opportunity.badge}</span>
          {/if}
          <h3 class="opportunity-title">{opportunity.title}</h3>
          {#if opportunity.description}
            <p class="opportunity-description">{opportunity.description}</p>
          {/if}
          {#if opportunity.cta_text && opportunity.cta_link}
            <a href={opportunity.cta_link} class="opportunity-cta">{opportunity.cta_text}</a>
          {/if}
        </div>
      {/each}
    </div>
  </div>
</section>

<style>
  .opportunities-section {
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

  .opportunities-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 30px;
  }

  .opportunity-card {
    background: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    position: relative;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    display: flex;
    flex-direction: column;
  }

  .opportunity-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
  }

  .badge {
    display: inline-block;
    padding: 5px 12px;
    background: #0066cc;
    color: white;
    font-size: 0.75rem;
    font-weight: 600;
    border-radius: 20px;
    margin-bottom: 15px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    align-self: flex-start;
  }

  .opportunity-title {
    font-size: 1.5rem;
    color: #1a1a1a;
    margin-bottom: 15px;
    font-weight: 600;
  }

  .opportunity-description {
    font-size: 1rem;
    color: #666;
    line-height: 1.6;
    margin-bottom: 20px;
    flex-grow: 1;
  }

  .opportunity-cta {
    display: inline-block;
    padding: 12px 24px;
    background: #0066cc;
    color: white;
    border-radius: 5px;
    font-weight: 500;
    text-decoration: none;
    text-align: center;
    transition: background 0.2s ease;
    align-self: flex-start;
  }

  .opportunity-cta:hover {
    background: #0052a3;
    text-decoration: none;
  }

  @media (max-width: 768px) {
    .section-title {
      font-size: 2rem;
    }

    .opportunities-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

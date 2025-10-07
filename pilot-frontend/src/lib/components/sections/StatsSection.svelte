<script>
  let { data } = $props();
</script>

<section class="stats-section">
  <div class="container">
    <!-- {#if data.title}
      <h2 class="section-title">{data.title}</h2>
    {/if} -->

    <div class="stats-grid">
      {#each data.stats as stat, index}
        <div class="stat-card" class:major={index < 2} class:minor={index >= 2}>
          <div class="stat-number">{stat.number}</div>
          <div class="stat-label">{stat.label}</div>
          {#if stat.description}
            <p class="stat-description">{stat.description}</p>
          {/if}
          {#if stat.cta_text && stat.cta_link}
            <a href={stat.cta_link} class="stat-cta">{stat.cta_text}</a>
          {/if}
        </div>
      {/each}
    </div>
  </div>
</section>

<style>
  .stats-section {
    padding: 60px 20px;
    /* background: #f8f9fa; */
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
  }

  .stats-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 30px;
  }

  .stat-card {
    padding: 30px;
    border-radius: 4px;
    box-shadow: 0px 0px 26px rgba(0, 0, 0, 0.09);
    text-align: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    color: white;
    text-align: left;
    background: rgba(255, 255, 255, 0.05);
  }

  .stat-card.major {
    grid-column: span 3;
  }

  .stat-card.minor {
    grid-column: span 2;
  }

  .stat-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
  }

  .stat-number {
    font-size: 4rem;
    font-weight: 600;
    letter-spacing: -0.1rem;
    line-height: 1em;
  }

  .stat-label {
    font-size: 1.1rem;
    margin-bottom: 10px;
    line-height: 1.2em;
    font-weight: 600;
  }

  .stat-description {
    font-size: 0.95rem;
    color: #666;
    margin-bottom: 15px;
  }

  .stat-cta {
    margin-top: 2rem;
    display: inline-block;
    padding: 10px 20px;
    color: white;
    border-radius: 5px;
    font-weight: 500;
    text-decoration: none;
    transition: background 0.2s ease;
    background: none;
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 1rem 0 2rem 0;
  }

  .stat-cta:hover {
    border-color: white;
  }

  @media (max-width: 768px) {
    .section-title {
      font-size: 2rem;
    }

    .stats-grid {
      grid-template-columns: 1fr;
    }

    .stat-number {
      font-size: 2.5rem;
    }
  }
</style>

<script>
  let { data } = $props();
</script>

<section class="rich-content-section">
  <div class="container">
    {#if data.title}
      <h2 class="section-title">{data.title}</h2>
    {/if}

    <div class="rich-content">
      {#each data.content as block}
        {#if block.type === 'paragraph'}
          <div class="content-paragraph">
            {@html block.value}
          </div>
        {:else if block.type === 'list'}
          <ul class="content-list">
            {#each block.value as item}
              <li>{item}</li>
            {/each}
          </ul>
        {:else if block.type === 'heading'}
          <h3 class="content-heading">{block.value}</h3>
        {/if}
      {/each}
    </div>
  </div>
</section>

<style>
  .rich-content-section {
    padding: 60px 20px;
    background: white;
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

  .rich-content {
    background: #f8f9fa;
    padding: 40px;
    border-radius: 8px;
  }

  .content-paragraph {
    font-size: 1.1rem;
    color: #333;
    line-height: 1.8;
    margin-bottom: 20px;
  }

  .content-paragraph :global(p) {
    margin-bottom: 15px;
  }

  .content-paragraph :global(a) {
    color: #0066cc;
    text-decoration: underline;
  }

  .content-paragraph :global(a:hover) {
    color: #0052a3;
  }

  .content-list {
    font-size: 1.1rem;
    color: #333;
    line-height: 1.8;
    margin: 20px 0;
    padding-left: 30px;
  }

  .content-list li {
    margin-bottom: 10px;
  }

  .content-heading {
    font-size: 1.8rem;
    color: #1a1a1a;
    margin-top: 30px;
    margin-bottom: 20px;
    font-weight: 600;
  }

  @media (max-width: 768px) {
    .section-title {
      font-size: 2rem;
    }

    .rich-content {
      padding: 25px;
    }

    .content-paragraph,
    .content-list {
      font-size: 1rem;
    }

    .content-heading {
      font-size: 1.5rem;
    }
  }
</style>

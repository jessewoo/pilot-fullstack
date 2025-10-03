<script>
  import DynamicPageBody from '$lib/components/DynamicPageBody.svelte';

  export let data;

  $: page = data.page;
</script>

<svelte:head>
  <title>{page.title}</title>
  {#if page.meta_description}
    <meta name="description" content={page.meta_description} />
  {/if}
</svelte:head>

<article class="dynamic-page" id={page.slug}>
  <div class="container">
    <h1>{page.title}</h1>

    {#if page.body && Array.isArray(page.body)}
      <DynamicPageBody body={page.body} />
    {:else if page.body}
      <div class="content">
        {@html page.body}
      </div>
    {/if}

    {#if page.content && Array.isArray(page.content)}
      <DynamicPageBody body={page.content} />
    {:else if page.content && !page.body}
      <div class="content">
        {@html page.content}
      </div>
    {/if}
  </div>
</article>

<style>
  .dynamic-page {
    padding: 60px 20px;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    background: white;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  h1 {
    color: #1a1a1a;
    font-size: 2.5rem;
    margin-bottom: 30px;
    border-bottom: 3px solid #0066cc;
    padding-bottom: 15px;
  }

  .content {
    line-height: 1.8;
    font-size: 1.1rem;
  }

  .content :global(h2) {
    color: #2c3e50;
    margin-top: 35px;
    margin-bottom: 15px;
    font-size: 1.8rem;
  }

  .content :global(h3) {
    color: #34495e;
    margin-top: 25px;
    margin-bottom: 12px;
    font-size: 1.4rem;
  }

  .content :global(p) {
    margin-bottom: 15px;
  }

  .content :global(img) {
    max-width: 100%;
    height: auto;
    border-radius: 4px;
    margin: 20px 0;
  }

  .content :global(ul), .content :global(ol) {
    margin: 15px 0;
    padding-left: 30px;
  }

  .content :global(li) {
    margin-bottom: 8px;
  }

  .content :global(blockquote) {
    border-left: 4px solid #0066cc;
    padding-left: 20px;
    margin: 20px 0;
    font-style: italic;
    color: #555;
  }

  .content :global(code) {
    background: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
  }

  .content :global(pre) {
    background: #f4f4f4;
    padding: 15px;
    border-radius: 4px;
    overflow-x: auto;
  }

  @media (max-width: 768px) {
    .container {
      padding: 25px;
    }

    h1 {
      font-size: 2rem;
    }
  }
</style>
<script>
  import { getImageUrl } from '$lib/utils/image.js';

  let { body } = $props();

  function executeScripts(node) {
    const scripts = node.querySelectorAll('script');
    scripts.forEach(script => {
      const newScript = document.createElement('script');
      Array.from(script.attributes).forEach(attr => {
        newScript.setAttribute(attr.name, attr.value);
      });
      newScript.textContent = script.textContent;
      script.parentNode.replaceChild(newScript, script);
    });
  }
</script>

{#if body && Array.isArray(body)}
  <div class="dynamic-body">
    {#each body as block}
      {#if block.type === 'paragraph'}
        <div class="body-paragraph">
          {@html block.value}
        </div>
      {:else if block.type === 'heading'}
        {#if block.value.level === 'h2'}
          <h2 class="body-heading-2">{block.value.text}</h2>
        {:else if block.value.level === 'h3'}
          <h3 class="body-heading-3">{block.value.text}</h3>
        {:else if block.value.level === 'h4'}
          <h4 class="body-heading-4">{block.value.text}</h4>
        {:else if block.value.level === 'h5'}
          <h5 class="body-heading-5">{block.value.text}</h5>
        {:else}
          <h6 class="body-heading-6">{block.value.text}</h6>
        {/if}
      {:else if block.type === 'image'}
        <figure class="body-image">
          <img
            src={getImageUrl(block.value.image.url)}
            alt={block.value.alt_text || block.value.image.title}
            width={block.value.image.width}
            height={block.value.image.height}
          />
          {#if block.value.caption}
            <figcaption>{block.value.caption}</figcaption>
          {/if}
        </figure>
      {:else if block.type === 'embed'}
        <div class="body-embed">
          {@html block.value}
        </div>
      {:else if block.type === 'list'}
        <ul class="body-list">
          {#each block.value as item}
            <li>{item}</li>
          {/each}
        </ul>
      {:else if block.type === 'list_with_links'}
        <div class="list-with-links">
          {#if block.value.title}
            <h3 class="list-title">{block.value.title}</h3>
          {/if}
          <ul class="links-list">
            {#each block.value.items as item}
              <li>
                <a href={item.link}>{item.text}</a>
              </li>
            {/each}
          </ul>
        </div>
      {:else if block.type === 'call_to_action'}
        <div class="call-to-action">
          {#if block.value.title}
            <h3 class="cta-title">{block.value.title}</h3>
          {/if}
          {#if block.value.text}
            <div class="cta-text">
              {@html block.value.text}
            </div>
          {/if}
          {#if block.value.button_text && block.value.button_url}
            <a href={block.value.button_url} class="cta-button">
              {block.value.button_text}
            </a>
          {/if}
        </div>
      {:else if block.type === 'html'}
        <div class="body-html" use:executeScripts>
          {@html block.value}
        </div>
      {:else if block.type === 'quote'}
        <blockquote class="body-quote">
          {@html block.value}
        </blockquote>
      {/if}
    {/each}
  </div>
{/if}

<style>
  .dynamic-body {
    line-height: 1.8;
    font-size: 1.1rem;
  }

  .body-paragraph {
    margin-bottom: 20px;
  }

  .body-paragraph :global(p) {
    margin-bottom: 15px;
  }

  .body-paragraph :global(a) {
    color: #0066cc;
    text-decoration: underline;
  }

  .body-paragraph :global(a:hover) {
    color: #0052a3;
  }

  .body-paragraph :global(b),
  .body-paragraph :global(strong) {
    font-weight: 600;
  }

  .body-heading-2 {
    color: #2c3e50;
    margin-top: 40px;
    margin-bottom: 20px;
    font-size: 2rem;
    font-weight: 600;
    border-bottom: 2px solid #e0e0e0;
    padding-bottom: 10px;
  }

  .body-heading-3 {
    color: #34495e;
    margin-top: 30px;
    margin-bottom: 15px;
    font-size: 1.5rem;
    font-weight: 600;
  }

  .body-heading-4 {
    color: #34495e;
    margin-top: 25px;
    margin-bottom: 12px;
    font-size: 1.3rem;
    font-weight: 600;
  }

  .body-heading-5,
  .body-heading-6 {
    color: #34495e;
    margin-top: 20px;
    margin-bottom: 10px;
    font-size: 1.1rem;
    font-weight: 600;
  }

  .body-image {
    margin: 30px 0;
    text-align: center;
  }

  .body-image img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  .body-image figcaption {
    margin-top: 10px;
    font-size: 0.9rem;
    color: #666;
    font-style: italic;
    text-align: center;
  }

  .body-embed {
    margin: 40px 0;
    position: relative;
    width: 100%;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
    height: 0;
    overflow: hidden;
  }

  .body-embed :global(iframe) {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 8px;
    border: none;
  }

  .body-embed :global(div) {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }

  .body-list {
    margin: 20px 0;
    padding-left: 30px;
  }

  .body-list li {
    margin-bottom: 10px;
  }

  .list-with-links {
    margin: 30px 0;
    padding: 25px;
    background: #f8f9fa;
    border-radius: 8px;
    border-left: 4px solid #0066cc;
  }

  .list-title {
    color: #1a1a1a;
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 20px;
  }

  .links-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .links-list li {
    margin-bottom: 12px;
    padding-left: 25px;
    position: relative;
  }

  .links-list li::before {
    content: "→";
    position: absolute;
    left: 0;
    color: #0066cc;
    font-weight: bold;
  }

  .links-list a {
    color: #0066cc;
    text-decoration: none;
    font-size: 1.05rem;
    transition: color 0.2s ease;
  }

  .links-list a:hover {
    color: #0052a3;
    text-decoration: underline;
  }

  .call-to-action {
    margin: 40px 0;
    padding: 30px;
    background: linear-gradient(135deg, #0066cc 0%, #0052a3 100%);
    border-radius: 12px;
    text-align: center;
    color: white;
    box-shadow: 0 4px 12px rgba(0, 102, 204, 0.3);
  }

  .cta-title {
    color: white;
    font-size: 1.8rem;
    font-weight: 600;
    margin-bottom: 15px;
  }

  .cta-text {
    color: white;
    font-size: 1.1rem;
    line-height: 1.6;
    margin-bottom: 25px;
  }

  .cta-text :global(p) {
    color: white;
    margin-bottom: 10px;
  }

  .cta-button {
    display: inline-block;
    padding: 14px 32px;
    background: white;
    color: #0066cc;
    border-radius: 6px;
    font-weight: 600;
    font-size: 1.1rem;
    text-decoration: none;
    transition: all 0.2s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  }

  .cta-button:hover {
    background: #f0f0f0;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    text-decoration: none;
  }

  .body-html {
    margin: 30px 0;
  }

  .body-quote {
    border-left: 4px solid #0066cc;
    padding-left: 20px;
    margin: 25px 0;
    font-style: italic;
    color: #555;
    font-size: 1.1rem;
  }

  .body-quote :global(p) {
    margin-bottom: 10px;
  }

  @media (max-width: 768px) {
    .dynamic-body {
      font-size: 1rem;
    }

    .body-heading-2 {
      font-size: 1.6rem;
      margin-top: 30px;
    }

    .body-heading-3 {
      font-size: 1.3rem;
      margin-top: 25px;
    }

    .body-heading-4 {
      font-size: 1.2rem;
    }

    .body-image {
      margin: 20px 0;
    }

    .body-embed {
      margin: 20px 0;
    }
  }
</style>

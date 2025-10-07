<script>
  import StatsSection from './sections/StatsSection.svelte';
  import LinksSection from './sections/LinksSection.svelte';
  import OpportunitiesSection from './sections/OpportunitiesSection.svelte';
  import ProjectHighlightsSection from './sections/ProjectHighlightsSection.svelte';
  import NewsSection from './sections/NewsSection.svelte';
  import RichContentSection from './sections/RichContentSection.svelte';

  let { page } = $props();
</script>

{#if page}
  <div class="wrap">
    <div class="home-head">
        <div class="real-hero">
        <h1>
          <strong>{page.hero_title}</strong>
        </h1>
        <section class="about">
          <div class="inner">
            <div class="intro" style="font-size: 1.25rem">
              {page.hero_subtitle}
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
  {#if page.content_sections && page.content_sections.length > 0}
    <div class="page-wrap">
      <main id="maincontent" class="page">
        {#each page.content_sections as section}
          {#if section.type === 'stats_section'}
            <StatsSection data={section.value} />
          {:else if section.type === 'links_section'}
            <LinksSection data={section.value} />
          {:else if section.type === 'opportunities_section'}
            <OpportunitiesSection data={section.value} />
          {:else if section.type === 'project_highlights'}
            <ProjectHighlightsSection data={section.value} />
          {:else if section.type === 'news_section'}
            <NewsSection data={section.value} />
          {:else if section.type === 'rich_content_section'}
            <RichContentSection data={section.value} />
          {/if}
        {/each}
      </main>
    </div>
  {/if}
{:else}
  <div class="container">
    <h1>Welcome</h1>
    <p>Loading homepage content...</p>
  </div>
{/if}

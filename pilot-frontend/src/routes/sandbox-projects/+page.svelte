<script>
  import DynamicPageBody from '$lib/components/DynamicPageBody.svelte';

  export let data;

  $: page = data.page;
  $: projects = data.projects || [];
</script>

<svelte:head>
  <title>{page.title}</title>
  {#if page.search_description}
    <meta name="description" content={page.search_description} />
  {/if}
</svelte:head>

<article class="sandbox-projects-page">
  <div class="container">
    <h1>{page.title}</h1>

    <!-- Page Content -->
    {#if page.content && Array.isArray(page.content)}
      <div class="page-intro">
        <DynamicPageBody body={page.content} />
      </div>
    {/if}

    <!-- Projects Grid -->
    {#if projects.length > 0}
      <div class="projects-section">
        <h2>Available Projects</h2>
        <div class="projects-grid">
          {#each projects as project}
            <a href="/sandbox-projects/{project.slug}" class="project-card">
              <div class="project-type-badge" data-type={project.project_type}>
                {project.project_type}
              </div>
              <h3>{project.title}</h3>
              <div class="project-link">View Project →</div>
            </a>
          {/each}
        </div>
      </div>
    {:else}
      <p class="no-projects">No sandbox projects available at this time.</p>
    {/if}
  </div>
</article>

<style>
  .sandbox-projects-page {
    padding: 60px 20px;
    background: #f8f9fa;
    min-height: 100vh;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
  }

  h1 {
    color: #1a1a1a;
    font-size: 2.5rem;
    margin-bottom: 30px;
    border-bottom: 3px solid #0066cc;
    padding-bottom: 15px;
    background: white;
    padding: 30px;
    border-radius: 8px 8px 0 0;
  }

  .page-intro {
    background: white;
    padding: 0 30px 30px;
    border-radius: 0 0 8px 8px;
    margin-bottom: 40px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  .page-intro :global(p) {
    line-height: 1.8;
    font-size: 1.1rem;
    color: #333;
  }

  .projects-section {
    margin-top: 40px;
  }

  .projects-section h2 {
    font-size: 2rem;
    color: #2c3e50;
    margin-bottom: 30px;
  }

  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 24px;
    margin-top: 20px;
  }

  .project-card {
    background: white;
    padding: 24px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    text-decoration: none;
    color: inherit;
    transition: all 0.3s ease;
    position: relative;
    border: 2px solid transparent;
  }

  .project-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
    border-color: #0066cc;
  }

  .project-type-badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 4px;
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: capitalize;
    margin-bottom: 12px;
  }

  .project-type-badge[data-type="classroom"] {
    background: #e3f2fd;
    color: #1976d2;
  }

  .project-type-badge[data-type="pilot"] {
    background: #f3e5f5;
    color: #7b1fa2;
  }

  .project-type-badge[data-type="startup"] {
    background: #e8f5e9;
    color: #388e3c;
  }

  .project-card h3 {
    font-size: 1.3rem;
    color: #1a1a1a;
    margin-bottom: 12px;
    line-height: 1.4;
  }

  .project-link {
    color: #0066cc;
    font-weight: 500;
    margin-top: 12px;
    transition: color 0.2s;
  }

  .project-card:hover .project-link {
    color: #004499;
  }

  .no-projects {
    text-align: center;
    padding: 40px;
    background: white;
    border-radius: 8px;
    color: #666;
    font-size: 1.1rem;
  }

  @media (max-width: 768px) {
    .sandbox-projects-page {
      padding: 40px 15px;
    }

    h1 {
      font-size: 2rem;
      padding: 20px;
    }

    .page-intro {
      padding: 0 20px 20px;
    }

    .projects-grid {
      grid-template-columns: 1fr;
      gap: 16px;
    }

    .projects-section h2 {
      font-size: 1.5rem;
    }
  }
</style>

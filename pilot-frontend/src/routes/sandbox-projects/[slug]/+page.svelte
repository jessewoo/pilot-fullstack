<script>
  export let data;

  $: project = data.project;

  // Helper to get image URL
  function getImageUrl(image) {
    if (!image) return null;
    // Return the image URL as-is (relative paths work with nginx proxy)
    return image.url;
  }

  // Helper to get project type label
  function getProjectTypeLabel(type) {
    const labels = {
      'classroom': 'Classroom',
      'pilot': 'Pilot',
      'startup': 'Startup'
    };
    return labels[type] || type;
  }

  // Helper to get hosting platform label
  function getHostingPlatformLabel(platform) {
    const labels = {
      'jetstream2': 'JetStream2',
      'huggingface': 'Hugging Face',
      'national_data_platform': 'National Data Platform',
      'other': 'Other'
    };
    return labels[platform] || platform;
  }
</script>

<svelte:head>
  <title>{project.title} - NAIRR Sandbox</title>
  {#if project.search_description}
    <meta name="description" content={project.search_description} />
  {/if}
</svelte:head>

<article class="project-detail">
  <!-- Breadcrumbs -->
  {#if project.breadcrumbs && project.breadcrumbs.length > 0}
    <nav class="breadcrumbs">
      <div class="container">
        {#each project.breadcrumbs as crumb, i}
          {#if i > 0}
            <span class="separator">/</span>
          {/if}
          {#if crumb.url && i < project.breadcrumbs.length - 1}
            <a href={crumb.url}>{crumb.title}</a>
          {:else if i > 0}
            <span class="current">{crumb.title}</span>
          {/if}
        {/each}
      </div>
    </nav>
  {/if}

  <!-- Hero Section -->
  <div class="hero">
    <div class="container">
      <div class="hero-content">
        <div class="badges">
          {#if project.project_type}
            <span class="badge project-type" data-type={project.project_type}>
              {getProjectTypeLabel(project.project_type)}
            </span>
          {/if}
          {#if project.hosting_platform}
            <span class="badge hosting-platform">
              {getHostingPlatformLabel(project.hosting_platform)}
            </span>
          {/if}
        </div>

        <h1>{project.title}</h1>

        {#if project.subtitle}
          <p class="subtitle">{project.subtitle}</p>
        {/if}

        {#if project.jupyter_lab_url}
          <div class="cta-button-wrapper">
            <a href={project.jupyter_lab_url} class="cta-button" target="_blank" rel="noopener noreferrer">
              {project.jupyter_cta_text || 'Launch JupyterLab'} ↗
            </a>
          </div>
        {/if}
      </div>

      {#if project.project_image}
        <div class="hero-image">
          <img src={getImageUrl(project.project_image)} alt={project.project_image.title || project.title} />
        </div>
      {/if}
    </div>
  </div>

  <!-- Main Content -->
  <div class="main-content">
    <div class="container">
      <div class="content-grid">
        <!-- Left Column - Main Info -->
        <div class="main-column">
          {#if project.project_info}
            <section class="section">
              <h2>Project Information</h2>
              <div class="rich-text">
                {@html project.project_info}
              </div>
            </section>
          {/if}

          {#if project.abstract}
            <section class="section">
              <h2>Abstract</h2>
              <div class="rich-text">
                {@html project.abstract}
              </div>
            </section>
          {/if}

          {#if project.references}
            <section class="section">
              <h2>References</h2>
              <div class="rich-text">
                {@html project.references}
              </div>
            </section>
          {/if}
        </div>

        <!-- Right Column - Sidebar -->
        <aside class="sidebar">
          {#if project.principal_investigator}
            <div class="info-card">
              <h3>Principal Investigator</h3>
              {#if project.principal_investigator_image}
                <div class="pi-image">
                  <img src={getImageUrl(project.principal_investigator_image)} alt={project.principal_investigator} />
                </div>
              {/if}
              <p class="pi-name">{project.principal_investigator}</p>
              {#if project.principal_investigator_url}
                <a href={project.principal_investigator_url} class="pi-link" target="_blank" rel="noopener noreferrer">
                  Visit Website ↗
                </a>
              {/if}
            </div>
          {/if}

          {#if project.institution}
            <div class="info-card">
              <h3>Institution</h3>
              <p>{project.institution}</p>
            </div>
          {/if}

          {#if project.github_repo_url}
            <div class="info-card">
              <h3>Resources</h3>
              <a href={project.github_repo_url} class="resource-link" target="_blank" rel="noopener noreferrer">
                <svg width="20" height="20" viewBox="0 0 16 16" fill="currentColor">
                  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
                View on GitHub
              </a>
            </div>
          {/if}
        </aside>
      </div>
    </div>
  </div>
</article>

<style>
  .project-detail {
    min-height: 100vh;
    background: #f8f9fa;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }

  /* Breadcrumbs */
  .breadcrumbs {
    background: white;
    border-bottom: 1px solid #e0e0e0;
    padding: 12px 0;
    font-size: 0.9rem;
  }

  .breadcrumbs a {
    color: #0066cc;
    text-decoration: none;
  }

  .breadcrumbs a:hover {
    text-decoration: underline;
  }

  .breadcrumbs .separator {
    margin: 0 8px;
    color: #999;
  }

  .breadcrumbs .current {
    color: #666;
  }

  /* Hero Section */
  .hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 60px 0;
  }

  .hero .container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    align-items: center;
  }

  .hero-content h1 {
    font-size: 2.5rem;
    margin-bottom: 16px;
    line-height: 1.2;
  }

  .subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
    margin-bottom: 24px;
  }

  .badges {
    display: flex;
    gap: 12px;
    margin-bottom: 20px;
    flex-wrap: wrap;
  }

  .badge {
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: capitalize;
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
  }

  .badge.project-type[data-type="classroom"] {
    background: #e3f2fd;
    color: #1976d2;
  }

  .badge.project-type[data-type="pilot"] {
    background: #f3e5f5;
    color: #7b1fa2;
  }

  .badge.project-type[data-type="startup"] {
    background: #e8f5e9;
    color: #388e3c;
  }

  .cta-button-wrapper {
    margin-top: 30px;
  }

  .cta-button {
    display: inline-block;
    background: white;
    color: #667eea;
    padding: 14px 32px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }

  .cta-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
  }

  .hero-image {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  }

  .hero-image img {
    width: 100%;
    height: auto;
    display: block;
  }

  /* Main Content */
  .main-content {
    padding: 60px 0;
  }

  .content-grid {
    display: grid;
    grid-template-columns: 1fr 350px;
    gap: 40px;
  }

  .main-column {
    background: white;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .section {
    margin-bottom: 40px;
  }

  .section:last-child {
    margin-bottom: 0;
  }

  .section h2 {
    font-size: 1.8rem;
    color: #2c3e50;
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 2px solid #e0e0e0;
  }

  .rich-text {
    line-height: 1.8;
    color: #333;
  }

  .rich-text :global(p) {
    margin-bottom: 16px;
  }

  .rich-text :global(a) {
    color: #0066cc;
    text-decoration: none;
  }

  .rich-text :global(a:hover) {
    text-decoration: underline;
  }

  /* Sidebar */
  .sidebar {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }

  .info-card {
    background: white;
    padding: 24px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .info-card h3 {
    font-size: 1.2rem;
    color: #2c3e50;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 2px solid #e0e0e0;
  }

  .info-card p {
    color: #555;
    line-height: 1.6;
  }

  .pi-image {
    margin-bottom: 16px;
    border-radius: 8px;
    overflow: hidden;
  }

  .pi-image img {
    width: 100%;
    height: auto;
    display: block;
  }

  .pi-name {
    font-weight: 600;
    font-size: 1.1rem;
    color: #1a1a1a;
    margin-bottom: 12px;
  }

  .pi-link {
    display: inline-block;
    color: #0066cc;
    text-decoration: none;
    font-weight: 500;
  }

  .pi-link:hover {
    text-decoration: underline;
  }

  .resource-link {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #0066cc;
    text-decoration: none;
    font-weight: 500;
    padding: 12px 16px;
    background: #f8f9fa;
    border-radius: 6px;
    transition: all 0.2s;
  }

  .resource-link:hover {
    background: #e3f2fd;
  }

  /* Responsive */
  @media (max-width: 968px) {
    .hero .container {
      grid-template-columns: 1fr;
    }

    .hero-image {
      order: -1;
    }

    .content-grid {
      grid-template-columns: 1fr;
    }

    .sidebar {
      order: -1;
    }
  }

  @media (max-width: 768px) {
    .hero {
      padding: 40px 0;
    }

    .hero-content h1 {
      font-size: 2rem;
    }

    .main-content {
      padding: 40px 0;
    }

    .main-column {
      padding: 24px;
    }

    .section h2 {
      font-size: 1.5rem;
    }
  }
</style>

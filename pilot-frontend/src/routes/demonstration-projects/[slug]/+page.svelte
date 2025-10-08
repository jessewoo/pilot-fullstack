<script>
  export let data;

  $: project = data.project;

  // Helper to get image URL
  function getImageUrl(image) {
    if (!image) return null;
    return image.url;
  }

  // Helper to get project type label
  function getProjectTypeLabel(type) {
    const labels = {
      'research': 'Research',
      'education': 'Education',
      'infrastructure': 'Infrastructure',
      'application': 'Application',
      'other': 'Other'
    };
    return labels[type] || type;
  }
</script>

<svelte:head>
  <title>{project.title} - NAIRR Demonstration Project</title>
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
        {#if project.project_type}
          <div class="badge" data-type={project.project_type}>
            {getProjectTypeLabel(project.project_type)}
          </div>
        {/if}

        <h1>{project.title}</h1>

        {#if project.subtitle}
          <p class="subtitle">{project.subtitle}</p>
        {/if}

        {#if project.project_intro}
          <div class="project-intro">
            {@html project.project_intro}
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

  <!-- Main Content - 2 Column Layout -->
  <div class="main-content">
    <div class="container">
      <div class="content-grid">
        <!-- Left Column - Main Project Information -->
        <div class="main-column">
          {#if project.project_info}
            <section class="section">
              <h2>Project Information</h2>
              <div class="rich-text">
                {@html project.project_info}
              </div>
            </section>
          {/if}

          {#if project.more_information}
            <section class="section">
              <h2>More Information</h2>
              <div class="rich-text">
                {@html project.more_information}
              </div>
            </section>
          {/if}
        </div>

        <!-- Right Column - Sidebar with Project Lead and Team -->
        <aside class="sidebar">
          <!-- Project Lead -->
          {#if project.project_lead_name}
            <div class="info-card">
              <h3>Project Lead</h3>
              {#if project.project_lead_image}
                <div class="lead-image">
                  <img src={getImageUrl(project.project_lead_image)} alt={project.project_lead_name} />
                </div>
              {/if}
              <p class="lead-name">{project.project_lead_name}</p>
              {#if project.project_lead_institution}
                <p class="lead-institution">{project.project_lead_institution}</p>
              {/if}
            </div>
          {/if}

          <!-- Key Team Members -->
          {#if project.team_members && project.team_members.length > 0}
            <div class="info-card">
              <h3>Key Team Members</h3>
              <div class="team-list">
                {#each project.team_members as member}
                  <div class="team-member">
                    {#if member.photo}
                      <div class="member-photo">
                        <img src={getImageUrl(member.photo)} alt={member.name} />
                      </div>
                    {/if}
                    <div class="member-info">
                      <p class="member-name">{member.name}</p>
                      {#if member.role}
                        <p class="member-role">{member.role}</p>
                      {/if}
                      {#if member.institution}
                        <p class="member-institution">{member.institution}</p>
                      {/if}
                    </div>
                  </div>
                {/each}
              </div>
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

  .project-intro {
    font-size: 1.05rem;
    line-height: 1.7;
    opacity: 0.95;
    margin-top: 20px;
  }

  .project-intro :global(p) {
    margin-bottom: 12px;
  }

  .project-intro :global(p:last-child) {
    margin-bottom: 0;
  }

  .badge {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: capitalize;
    margin-bottom: 20px;
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
  }

  .badge[data-type="research"] {
    background: #e3f2fd;
    color: #1976d2;
  }

  .badge[data-type="education"] {
    background: #f3e5f5;
    color: #7b1fa2;
  }

  .badge[data-type="infrastructure"] {
    background: #e8f5e9;
    color: #388e3c;
  }

  .badge[data-type="application"] {
    background: #fff3e0;
    color: #f57c00;
  }

  .badge[data-type="other"] {
    background: #f5f5f5;
    color: #616161;
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

  /* Main Content - 2 Column Layout */
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

  /* Project Lead */
  .lead-image {
    margin-bottom: 16px;
    border-radius: 8px;
    overflow: hidden;
  }

  .lead-image img {
    width: 100%;
    height: auto;
    display: block;
  }

  .lead-name {
    font-weight: 600;
    font-size: 1.1rem;
    color: #1a1a1a;
    margin-bottom: 8px;
  }

  .lead-institution {
    color: #555;
    font-size: 0.95rem;
  }

  /* Team Members */
  .team-list {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .team-member {
    display: flex;
    gap: 12px;
    align-items: start;
  }

  .member-photo {
    flex-shrink: 0;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    overflow: hidden;
  }

  .member-photo img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .member-info {
    flex: 1;
  }

  .member-name {
    font-weight: 600;
    color: #1a1a1a;
    margin-bottom: 4px;
  }

  .member-role {
    font-size: 0.9rem;
    color: #0066cc;
    margin-bottom: 2px;
  }

  .member-institution {
    font-size: 0.85rem;
    color: #666;
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

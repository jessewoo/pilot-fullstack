<script>
  import { getImageUrl } from '$lib/utils/image.js';

  let { data } = $props();

  let currentIndex = $state(0);
  const itemsPerPage = 3;

  const totalPages = $derived(Math.ceil(data.projects.length / itemsPerPage));
  const visibleProjects = $derived(
    data.projects.slice(currentIndex * itemsPerPage, (currentIndex + 1) * itemsPerPage)
  );

  function nextSlide() {
    if (currentIndex < totalPages - 1) {
      currentIndex++;
    }
  }

  function prevSlide() {
    if (currentIndex > 0) {
      currentIndex--;
    }
  }
</script>

<section class="project-highlights-section">
  <div class="container">
    {#if data.section_title}
      <h2 class="section-title">{data.section_title}</h2>
    {/if}

    <div class="carousel-wrapper">
      <button
        class="carousel-arrow prev"
        onclick={prevSlide}
        disabled={currentIndex === 0}
        aria-label="Previous projects"
      >
        ←
      </button>

      <div class="projects-grid">
        {#each visibleProjects as project}
          <a href={project.link_url} class="project-card">
            {#if project.image}
              <div class="project-image">
                <img src={getImageUrl(project.image.url)} alt={project.image.title} width={project.image.width} height={project.image.height} />
              </div>
            {/if}
            <div class="project-content">
              <h3 class="project-title">{project.title}</h3>
              {#if project.authors}
                <p class="project-authors">{project.authors}</p>
              {/if}
              {#if project.description}
                <p class="project-description">{project.description}</p>
              {/if}
              {#if project.tags && project.tags.length > 0 && project.tags[0]}
                <div class="project-tags">
                  {#each project.tags as tag}
                    {#if tag}
                      <span class="tag">{tag}</span>
                    {/if}
                  {/each}
                </div>
              {/if}
              {#if project.link_text}
                <span class="project-link">{project.link_text} →</span>
              {:else}
                <span class="project-link">Learn More →</span>
              {/if}
            </div>
          </a>
        {/each}
      </div>

      <button
        class="carousel-arrow next"
        onclick={nextSlide}
        disabled={currentIndex === totalPages - 1}
        aria-label="Next projects"
      >
        →
      </button>
    </div>

    {#if totalPages > 1}
      <div class="carousel-dots">
        {#each Array(totalPages) as _, index}
          <button
            class="dot"
            class:active={index === currentIndex}
            onclick={() => currentIndex = index}
            aria-label={`Go to page ${index + 1}`}
          ></button>
        {/each}
      </div>
    {/if}
  </div>
</section>

<style>
  .project-highlights-section {
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

  .carousel-wrapper {
    position: relative;
    display: flex;
    align-items: center;
    gap: 20px;
  }

  .carousel-arrow {
    flex-shrink: 0;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: 2px solid #0066cc;
    background: white;
    color: #0066cc;
    font-size: 1.5rem;
    cursor: pointer;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .carousel-arrow:hover:not(:disabled) {
    background: #0066cc;
    color: white;
    transform: scale(1.1);
  }

  .carousel-arrow:disabled {
    opacity: 0.3;
    cursor: not-allowed;
  }

  .carousel-arrow.prev {
    margin-right: 10px;
  }

  .carousel-arrow.next {
    margin-left: 10px;
  }

  .projects-grid {
    flex: 1;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
  }

  .carousel-dots {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 30px;
  }

  .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    border: 2px solid #0066cc;
    background: white;
    cursor: pointer;
    transition: all 0.2s ease;
    padding: 0;
  }

  .dot:hover {
    transform: scale(1.2);
  }

  .dot.active {
    background: #0066cc;
  }

  .project-card {
    display: block;
    background: #f8f9fa;
    border-radius: 8px;
    overflow: hidden;
    text-decoration: none;
    color: inherit;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  .project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
    text-decoration: none;
  }

  .project-image {
    width: 100%;
    height: 220px;
    overflow: hidden;
    background: #e0e0e0;
  }

  .project-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .project-content {
    padding: 25px;
  }

  .project-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #1a1a1a;
    margin-bottom: 10px;
    line-height: 1.4;
  }

  .project-authors {
    font-size: 0.95rem;
    color: #666;
    margin-bottom: 10px;
    font-style: italic;
  }

  .project-description {
    font-size: 1rem;
    color: #555;
    line-height: 1.6;
    margin-bottom: 15px;
  }

  .project-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 15px;
  }

  .tag {
    display: inline-block;
    padding: 4px 10px;
    background: #0066cc;
    color: white;
    font-size: 0.75rem;
    border-radius: 12px;
    font-weight: 500;
  }

  .project-link {
    display: inline-block;
    color: #0066cc;
    font-weight: 500;
    transition: transform 0.2s ease;
  }

  .project-card:hover .project-link {
    transform: translateX(3px);
  }

  @media (max-width: 1024px) {
    .projects-grid {
      grid-template-columns: repeat(2, 1fr);
    }

    .carousel-arrow {
      width: 40px;
      height: 40px;
      font-size: 1.2rem;
    }
  }

  @media (max-width: 768px) {
    .section-title {
      font-size: 2rem;
    }

    .carousel-wrapper {
      flex-direction: column;
      gap: 15px;
    }

    .carousel-arrow {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      z-index: 10;
    }

    .carousel-arrow.prev {
      left: -10px;
      margin-right: 0;
    }

    .carousel-arrow.next {
      right: -10px;
      margin-left: 0;
    }

    .projects-grid {
      grid-template-columns: 1fr;
      padding: 0 20px;
    }
  }
</style>

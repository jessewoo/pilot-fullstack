import { error } from '@sveltejs/kit';
import { getPageBySlugUpdated, getDemonstrationProjects } from '$lib/api/wagtail';

export async function load() {
  const page = await getPageBySlugUpdated('demonstration-projects');
  const projects = await getDemonstrationProjects();

  if (!page) {
    throw error(404, 'Page not found');
  }

  return {
    page,
    projects
  };
}

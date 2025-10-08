import { error } from '@sveltejs/kit';
import { getPageBySlugUpdated, getSandboxProjects } from '$lib/api/wagtail';

export async function load() {
  const page = await getPageBySlugUpdated('sandbox-projects');
  const projects = await getSandboxProjects();

  if (!page) {
    throw error(404, 'Page not found');
  }

  return {
    page,
    projects
  };
}

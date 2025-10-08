import { error } from '@sveltejs/kit';
import { getPageBySlugUpdated } from '$lib/api/wagtail';

export async function load({ params }) {
  const project = await getPageBySlugUpdated(params.slug);

  if (!project) {
    throw error(404, 'Project not found');
  }

  return {
    project
  };
}

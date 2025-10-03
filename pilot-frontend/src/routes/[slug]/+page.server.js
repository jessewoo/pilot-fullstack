import { error } from '@sveltejs/kit';
import { getPageBySlug, getPageBySlugUpdated } from '$lib/api/wagtail';

export async function load({ params }) {
  const page = await getPageBySlugUpdated(params.slug);

  // console.log('Fetched page:', page);
  
  if (!page) {
    throw error(404, 'Page not found');
  }
  
  return {
    page
  };
}
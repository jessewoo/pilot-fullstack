import { getPageBySlugUpdated } from '$lib/api/wagtail';

export async function load() {
  const page = await getPageBySlugUpdated('home-page');

  return {
    page
  };
}

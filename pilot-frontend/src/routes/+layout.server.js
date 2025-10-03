import { getNavigationMenus } from '$lib/api/wagtail.js';

export async function load() {
  const navigationData = await getNavigationMenus();

  return {
    navigationMenus: navigationData.items || []
  };
}

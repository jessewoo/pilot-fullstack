import axios from 'axios';
import { PUBLIC_WAGTAIL_API_URL } from '$env/static/public';

const API_URL = PUBLIC_WAGTAIL_API_URL || 'http://localhost:8000/api/v2';

export async function getPages() {
  try {
    const response = await axios.get(`${API_URL}/pages/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching pages:', error);
    return { items: [] };
  }
}

export async function getPageBySlug(slug) {
  try {
    const response = await axios.get(`${API_URL}/pages/`, {
      params: {
        slug: slug,
        fields: '*'
      }
    });
    
    if (response.data.items && response.data.items.length > 0) {
      return response.data.items[0];
    }
    return null;
  } catch (error) {
    console.error('Error fetching page getPageBySlug:', error);
    return null;
  }
}

export async function getPageBySlugUpdated(slug) {
  try {
    // console.log(`Fetching page from: ${API_URL}/page-by-slug/?slug=${slug}`);
    const response = await axios.get(`${API_URL}/page-by-slug/`, {
      params: {
        slug: slug
      }
    });

    // console.log('Page fetch response:', response.data);
    if (response.data) {
      return response.data;
    }

    return null;
  } catch (error) {
    if (error.response?.status === 404) {
      console.warn(`Page not found for slug: ${slug}`);
    } else {
      console.error('Error fetching page getPageBySlugUpdated:', error);
    }
    return null;
  }
}

export async function getPageById(id) {
  try {
    const response = await axios.get(`${API_URL}/pages/${id}/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching page by ID:', error);
    return null;
  }
}

// Fetch navigation menus from Wagtail API
export async function getNavigationMenus() {
  console.log('Fetching navigation menus from:', `${API_URL}/navigation_menus/`);

  try {
    const response = await axios.get(`${API_URL}/navigation_menus/`);

    // console.log('Fetched navigation menus RESPONSE:', response);

    return response.data;
  } catch (error) {
    if (error.response?.status === 404) {
      console.warn('Navigation menus endpoint not found');
    } else {
      console.error('Error fetching navigation - getNavigationMenus:', error.message);
    }
    return { items: [] };
  }
}

// Fetch sandbox projects list
export async function getSandboxProjects() {
  try {
    const response = await axios.get(`${API_URL}/sandbox-projects/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching sandbox projects:', error);
    return [];
  }
}

// Fetch demonstration projects list
export async function getDemonstrationProjects() {
  try {
    const response = await axios.get(`${API_URL}/demonstration-projects/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching demonstration projects:', error);
    return [];
  }
}
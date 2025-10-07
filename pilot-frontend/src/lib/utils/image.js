const IMAGE_DOMAIN = import.meta.env.PUBLIC_IMAGE_DOMAIN || 'http://localhost:8000';

/**
 * Get the full image URL by prepending the image domain if needed
 * @param {string} url - The image URL (can be relative or absolute)
 * @returns {string} The full image URL
 */
export function getImageUrl(url) {
  if (!url) return '';

  // If the URL already starts with http:// or https://, return as is
  if (url.startsWith('http://') || url.startsWith('https://')) {
    return url;
  }

  // Otherwise, prepend the image domain
  return `${IMAGE_DOMAIN}${url}`;
}

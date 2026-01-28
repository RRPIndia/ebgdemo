import eleventyNavigationPlugin from "@11ty/eleventy-navigation";

export default function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("bundle.css");
  eleventyConfig.addPassthroughCopy("CNAME");

  eleventyConfig.addPlugin(eleventyNavigationPlugin);
  eleventyConfig.addFilter("pathSegments", (url) => {
    return url
      .replace(/^\/|\/$/g, "")
      .split("/")
      .filter(Boolean);
  });	
};

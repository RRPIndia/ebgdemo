export default function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("bundle.css");
  eleventyConfig.addPassthroughCopy("CNAME");

  eleventyConfig.addFilter("pathSegments", (url) => {
    return url
      .replace(/^\/|\/$/g, "")
      .split("/")
      .filter(Boolean);
  });	

  return {
    dir: {
      input: ".",
      output: "_site"
    }
  };

}

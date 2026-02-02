export default function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("CNAME");

  eleventyConfig.amendLibrary("md", (md) => {
  md.renderer.rules.table_open = () =>
    '<div class="table-wrapper"><table>';

  md.renderer.rules.table_close = () =>
    		  '</table></div>';
});

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

// replace ` -- ` by typographic headings trigger a new slide
// headings with a caret (e.g., '##^ foo`) trigger a new vertical slide
module.exports = (markdown, options) => {
  return new Promise((resolve, reject) => {
    var lines = markdown.split("\n");
    var in_def_list = false;

    var in_code_block = false;

    for (var i = 0; i < lines.length; i++) {
      if (lines[i].startsWith("```")) {
        in_code_block = !in_code_block;
      }
      if (in_code_block) {
        lines[i] = lines[i].replaceAll(" ", " ");
        continue;
      }

      if (lines[i].startsWith("|") && lines[i].endsWith("|")) {
        lines[i] = lines[i].replaceAll(/ +/g, " ");
      }

      // typo dash
      lines[i] = lines[i]
        .replaceAll(" -- ", " &mdash; ")
        .replaceAll(" --- ", " &mdash; ");

      // definition list syntax:
      //
      // Term
      // : Definition line
      // : Definition second definition line
      // Not a part of definition
      //
      // multiple definitions in a list translate to several independent definitions
      // Term can't be a markdown link.
      if (lines[i].startsWith(":") && i > 0) {
        if (!in_def_list) {
          lines[i - 1] = "<dl>\n  <dt> " + lines[i - 1] + " </dt>";
          lines[i] = "  <dd> " + lines[i].substring(1) + " </dd>";
          in_def_list = true;
        } else {
          lines[i] = "  <dd> " + lines[i].substring(1) + " </dd>";
        }
      } else if (in_def_list) {
        in_def_list = false;
        lines[i] = "</dl>\n " + lines[i];
      }
    }
    markdown = lines.join("\n");

    return resolve(markdown);
  });
};

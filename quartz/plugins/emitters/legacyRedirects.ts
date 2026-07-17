import { FilePath, FullSlug, joinSegments } from "../../util/path"
import { QuartzEmitterPlugin } from "../types"
import fs from "fs"
import { dirname } from "path"

const REDIRECTS_FILE = "redirects.json"

/**
 * Emits redirect stubs for URLs from previous generations of the site
 * (WordPress-era /YYYY/MM/DD/slug/, old capitalized /Articles/<Category>/<Title+> paths, etc.)
 * so links and search-index entries pointing at them land on the current pages.
 *
 * Paths in redirects.json are written to the output verbatim — no slugification —
 * because the old URLs contain capital letters and literal "+" characters that
 * frontmatter aliases (which get slugified/lowercased) cannot reproduce.
 */
export const LegacyRedirects: QuartzEmitterPlugin = () => ({
  name: "LegacyRedirects",
  async *emit({ argv }) {
    let mapping: Record<string, string>
    try {
      mapping = JSON.parse(await fs.promises.readFile(REDIRECTS_FILE, "utf-8"))
    } catch {
      return // no redirects file, nothing to emit
    }

    for (const [oldPath, target] of Object.entries(mapping)) {
      const redirUrl = target === "" ? "/" : `/${target}`
      const canonical = joinSegments("https://rohitmalekar.in", target === "" ? "" : target)
      const dest = joinSegments(argv.output, (oldPath as FullSlug) + ".html") as FilePath
      await fs.promises.mkdir(dirname(dest), { recursive: true })
      await fs.promises.writeFile(
        dest,
        `<!DOCTYPE html>
<html lang="en-us">
<head>
<title>${target || "Home"}</title>
<link rel="canonical" href="${canonical}">
<meta name="robots" content="noindex">
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=${redirUrl}">
</head>
</html>
`,
      )
      yield dest
    }
  },
  async *partialEmit() {},
})

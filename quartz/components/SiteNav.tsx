import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

const links: { label: string; href: string; prefixes: string[] }[] = [
  { label: "Writing", href: "/articles/", prefixes: ["articles", "tags"] },
  { label: "Notes", href: "/notes/", prefixes: ["notes"] },
  { label: "Portfolio", href: "/portfolio/", prefixes: ["portfolio"] },
  { label: "About", href: "/about", prefixes: ["about", "work-with-me", "cv"] },
]

const SiteNav: QuartzComponent = ({ fileData }: QuartzComponentProps) => {
  const slug = (fileData.slug ?? "").toLowerCase()
  const section = slug.split("/")[0]
  return (
    <nav class="site-nav" aria-label="Primary">
      {links.map((l) => (
        <a
          href={l.href}
          class="site-nav-link"
          aria-current={l.prefixes.includes(section) ? "page" : undefined}
        >
          {l.label}
        </a>
      ))}
    </nav>
  )
}

export default (() => SiteNav) satisfies QuartzComponentConstructor

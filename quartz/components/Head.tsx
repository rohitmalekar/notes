import { i18n } from "../i18n"
import { FullSlug, getFileExtension, joinSegments, pathToRoot, simplifySlug } from "../util/path"
import { CSSResourceToStyleElement, JSResourceToScriptElement } from "../util/resources"
import { googleFontHref, googleFontSubsetHref } from "../util/theme"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { unescapeHTML } from "../util/escape"
import { CustomOgImagesEmitterName } from "../../.quartz/plugins"
export default (() => {
  const Head: QuartzComponent = ({
    cfg,
    fileData,
    externalResources,
    ctx,
  }: QuartzComponentProps) => {
    const titleSuffix = cfg.pageTitleSuffix ?? ""
    const baseTitle = fileData.frontmatter?.title ?? i18n(cfg.locale).propertyDefaults.title
    // Skip the suffix when the page title already carries the site name (e.g. the homepage)
    const title = baseTitle.includes(cfg.pageTitle) ? baseTitle : baseTitle + titleSuffix
    const description =
      fileData.frontmatter?.socialDescription ??
      fileData.frontmatter?.description ??
      unescapeHTML(fileData.description?.trim() ?? i18n(cfg.locale).propertyDefaults.description)

    const { css, js, additionalHead } = externalResources

    const url = new URL(`https://${cfg.baseUrl ?? "example.com"}`)
    const path = url.pathname as FullSlug
    const baseDir = fileData.slug === "404" ? path : pathToRoot(fileData.slug!)
    const iconPath = joinSegments(baseDir, "static/icon.png")

    // Url of current page (canonical form: no trailing "index"; folder pages keep a trailing slash
    // to match the sitemap and avoid canonical → 301 hops on GitHub Pages)
    const simpleSlug = simplifySlug(fileData.slug!)
    const isFolderPage = fileData.slug === "index" || fileData.slug!.endsWith("/index")
    const socialUrl =
      fileData.slug === "404"
        ? url.toString()
        : joinSegments(url.toString(), simpleSlug === "/" ? "" : simpleSlug).replace(
            /\/*$/,
            isFolderPage ? "/" : "",
          )

    const frontmatterType = fileData.frontmatter?.type as string | string[] | undefined
    const isArticle = Array.isArray(frontmatterType)
      ? frontmatterType.includes("Article")
      : frontmatterType === "Article"
    const publishedDate = fileData.dates?.published
    const modifiedDate = fileData.dates?.modified

    const siteUrl = `https://${cfg.baseUrl}/`
    const authorId = `https://${cfg.baseUrl}/#person`
    const jsonLd: object[] = []
    if (fileData.slug === "index") {
      jsonLd.push(
        {
          "@context": "https://schema.org",
          "@type": "Person",
          "@id": authorId,
          name: "Rohit Malekar",
          url: siteUrl,
          image: `https://${cfg.baseUrl}/Attachments/profile.jpg`,
          jobTitle:
            "Independent researcher and builder — funding systems and data for open source ecosystems",
          description:
            "Rohit Malekar designs funding systems, builds analytics tools, and researches governance for open source ecosystems, with work at Gitcoin, Metagov, Open Source Observer, and Scroll.",
          knowsAbout: [
            "grant program design",
            "quadratic funding",
            "ecosystem analytics",
            "DAO governance",
            "public goods funding",
            "data engineering",
            "product management",
          ],
          sameAs: [
            "https://www.linkedin.com/in/rohitmalekar/",
            "https://github.com/rohitmalekar",
            "https://twitter.com/RohitMalekar",
            "https://x.com/RohitMalekar",
            "https://warpcast.com/rohitmalekar.eth",
            "https://medium.com/@rohitmalekar",
            "https://hackernoon.com/u/rohitmalekar",
            "https://breathefeellove.in/",
          ],
        },
        {
          "@context": "https://schema.org",
          "@type": "WebSite",
          "@id": `https://${cfg.baseUrl}/#website`,
          url: siteUrl,
          name: cfg.pageTitle,
          publisher: { "@id": authorId },
        },
      )
    } else if (isArticle) {
      jsonLd.push({
        "@context": "https://schema.org",
        "@type": "Article",
        headline: baseTitle,
        description,
        url: socialUrl,
        datePublished: publishedDate?.toISOString(),
        dateModified: modifiedDate?.toISOString(),
        image: `https://${cfg.baseUrl}/${fileData.slug}-og-image.webp`,
        author: { "@type": "Person", "@id": authorId, name: "Rohit Malekar", url: siteUrl },
      })
    }

    const usesCustomOgImage = ctx.cfg.plugins.emitters.some(
      (e) => e.name === CustomOgImagesEmitterName,
    )
    const ogImageDefaultPath = `https://${cfg.baseUrl}/static/og-image.png`

    const coreStylesheet = css[0]?.content
    const coreScript = js.find(
      (r) => r.loadTime === "beforeDOMReady" && r.contentType === "external",
    )

    return (
      <head>
        <title>{title}</title>
        <meta charSet="utf-8" />
        {coreStylesheet && <link rel="preload" href={coreStylesheet} as="style" />}
        {coreScript && coreScript.contentType === "external" && (
          <link rel="preload" href={coreScript.src} as="script" />
        )}
        {cfg.theme.cdnCaching && cfg.theme.fontOrigin === "googleFonts" && (
          <>
            <link rel="preconnect" href="https://fonts.googleapis.com" />
            <link rel="preconnect" href="https://fonts.gstatic.com" />
            <link rel="stylesheet" href={googleFontHref(cfg.theme)} />
            {cfg.theme.typography.title && (
              <link rel="stylesheet" href={googleFontSubsetHref(cfg.theme, cfg.pageTitle)} />
            )}
          </>
        )}
        <link rel="preconnect" href="https://cdnjs.cloudflare.com" crossOrigin="anonymous" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />

        <meta name="og:site_name" content={cfg.pageTitle}></meta>
        <meta property="og:title" content={title} />
        <meta property="og:type" content={isArticle ? "article" : "website"} />
        {isArticle && publishedDate && (
          <meta property="article:published_time" content={publishedDate.toISOString()} />
        )}
        {isArticle && modifiedDate && (
          <meta property="article:modified_time" content={modifiedDate.toISOString()} />
        )}
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content={title} />
        <meta name="twitter:description" content={description} />
        <meta property="og:description" content={description} />
        <meta property="og:image:alt" content={description} />

        {!usesCustomOgImage && (
          <>
            <meta property="og:image" content={ogImageDefaultPath} />
            <meta property="og:image:url" content={ogImageDefaultPath} />
            <meta name="twitter:image" content={ogImageDefaultPath} />
            <meta
              property="og:image:type"
              content={`image/${getFileExtension(ogImageDefaultPath) ?? "png"}`}
            />
          </>
        )}

        {cfg.baseUrl && (
          <>
            <meta property="twitter:domain" content={cfg.baseUrl}></meta>
            <meta property="og:url" content={socialUrl}></meta>
            <meta property="twitter:url" content={socialUrl}></meta>
            {fileData.slug !== "404" && <link rel="canonical" href={socialUrl} />}
            <link
              rel="alternate"
              type="application/rss+xml"
              title={cfg.pageTitle}
              href={joinSegments(url.toString(), "index.xml")}
            />
          </>
        )}

        <link rel="icon" href={iconPath} />
        <meta name="description" content={description} />
        <meta name="generator" content="Quartz" />

        {jsonLd.map((obj) => (
          <script
            type="application/ld+json"
            dangerouslySetInnerHTML={{ __html: JSON.stringify(obj) }}
          />
        ))}

        {css.map((resource) => CSSResourceToStyleElement(resource, true))}
        {js
          .filter((resource) => resource.loadTime === "beforeDOMReady")
          .map((res) => JSResourceToScriptElement(res, true))}
        {additionalHead.map((resource) => {
          if (typeof resource === "function") {
            return resource(fileData)
          } else {
            return resource
          }
        })}
      </head>
    )
  }

  return Head
}) satisfies QuartzComponentConstructor

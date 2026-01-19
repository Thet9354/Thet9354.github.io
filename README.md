# Phoon Thet Pine — Portfolio

Portfolio website for Phoon Thet Pine, a web & app developer building AI apps and practical tools.

## Custom Domain Setup

This site is configured to use the custom domain `thetpine.dev`.

### DNS Configuration Required

To complete the domain connection, configure the following DNS records with your domain registrar:

#### For Apex Domain (thetpine.dev):
Add the following **A records**:
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

#### For www subdomain (www.thetpine.dev):
Add a **CNAME record** pointing to:
```
Thet9354.github.io
```

### Verification Steps

1. After configuring DNS records, wait for DNS propagation (can take up to 24-48 hours, but usually much faster)
2. Go to your repository settings on GitHub: `Settings` → `Pages`
3. Verify that the custom domain shows `thetpine.dev`
4. Enable "Enforce HTTPS" once the domain is verified (recommended)

### DNS Record Examples

If your domain registrar is:

**Cloudflare:**
- Type: `A`, Name: `@`, Content: `185.199.108.153`
- Type: `A`, Name: `@`, Content: `185.199.109.153`
- Type: `A`, Name: `@`, Content: `185.199.110.153`
- Type: `A`, Name: `@`, Content: `185.199.111.153`
- Type: `CNAME`, Name: `www`, Content: `Thet9354.github.io`

**Namecheap/GoDaddy:**
- Type: `A Record`, Host: `@`, Value: `185.199.108.153`
- Type: `A Record`, Host: `@`, Value: `185.199.109.153`
- Type: `A Record`, Host: `@`, Value: `185.199.110.153`
- Type: `A Record`, Host: `@`, Value: `185.199.111.153`
- Type: `CNAME Record`, Host: `www`, Value: `Thet9354.github.io`

### Troubleshooting

- **DNS not resolving?** Wait longer for DNS propagation and check your records with `dig thetpine.dev` or `nslookup thetpine.dev`
- **Certificate errors?** Make sure "Enforce HTTPS" is enabled in GitHub Pages settings after domain verification
- **404 errors?** Ensure the CNAME file in the repository contains only `thetpine.dev`

## License

© 2026 Phoon Thet Pine. All Rights Reserved.

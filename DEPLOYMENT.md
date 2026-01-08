# Walue AI - Frappe Cloud Deployment Guide

## Quick Deployment to Frappe Cloud

### Prerequisites
- Frappe Cloud account (sign up at https://frappecloud.com)
- GitHub repository: https://github.com/chinmaybhatk/walue_ai

### Deployment Steps

#### 1. Create/Access Your Frappe Cloud Site

1. Log in to your Frappe Cloud dashboard
2. Either create a new site or use an existing one
3. Note your site URL (e.g., `yoursite.frappe.cloud`)

#### 2. Install Walue AI App

**Option A: From GitHub (Recommended)**

1. In your Frappe Cloud dashboard, navigate to your site
2. Click on **Apps** in the left sidebar
3. Click **Install App** button
4. Select **Install from GitHub**
5. Enter repository details:
   - **Repository URL**: `https://github.com/chinmaybhatk/walue_ai`
   - **Branch**: `main`
6. Click **Install**
7. Wait for installation to complete (2-5 minutes)

**Option B: From Frappe Cloud App Store**

If the app is published to Frappe Cloud:
1. Go to **Apps** → **Browse Apps**
2. Search for "Walue AI"
3. Click **Install**

#### 3. Verify Installation

1. After installation completes, visit: `https://yoursite.frappe.cloud/home`
2. You should see the Walue AI landing page
3. The homepage is automatically set to `/home` via app hooks

#### 4. Set as Homepage (Optional)

If you want `/home` as your default homepage:

1. Go to **Website Settings** in Frappe Desk
2. Set **Home Page** to: `home`
3. Save

Alternatively, this is already configured in `hooks.py`:
```python
home_page = "home"
```

### Post-Deployment Configuration

#### Custom Domain Setup

1. In Frappe Cloud Dashboard:
   - Go to **Site** → **Domains**
   - Click **Add Domain**
   - Enter your custom domain (e.g., `walueai.com`)
   
2. Update DNS Records:
   - Add CNAME record pointing to your Frappe Cloud site
   - SSL certificate is automatically provisioned (Let's Encrypt)

#### Email Configuration

Configure outgoing email in:
- **Settings** → **Email Domain**
- Or use Frappe Cloud's built-in email

### Customization

#### Update Branding

Edit the landing page:
1. Enable Developer Mode:
   ```bash
   # Via bench console or Frappe Cloud terminal
   bench --site yoursite.frappe.cloud set-config developer_mode 1
   ```

2. Edit `walue_ai/www/home.html` in your GitHub repo
3. Commit and push changes
4. Frappe Cloud will auto-deploy updates

#### Add Custom Pages

Create new pages in `walue_ai/www/`:
- `about.html` → accessible at `/about`
- `pricing.html` → accessible at `/pricing`

### Monitoring & Maintenance

#### Check App Status

```bash
# List installed apps
bench --site yoursite.frappe.cloud list-apps

# Check app version
bench --site yoursite.frappe.cloud console
>>> frappe.get_installed_apps()
```

#### View Logs

In Frappe Cloud Dashboard:
- **Site** → **Logs** → **Error Logs**
- **Site** → **Logs** → **Web Logs**

#### Backup & Restore

Frappe Cloud provides automatic daily backups.

Manual backup:
1. **Site** → **Backups** → **Create Backup**
2. Download backups when needed

### Troubleshooting

#### App Not Installing

**Check repository access:**
- Ensure repository is public or Frappe Cloud has access
- Verify branch name is correct (`main`)

**Check logs:**
- View installation logs in Frappe Cloud dashboard

#### Landing Page Not Showing

**Verify routes:**
```python
# In hooks.py
website_route_rules = [
    {"from_route": "/home", "to_route": "home"},
]
```

**Clear cache:**
```bash
bench --site yoursite.frappe.cloud clear-cache
bench --site yoursite.frappe.cloud build
```

#### Updates Not Reflecting

**Rebuild assets:**
```bash
bench build --app walue_ai
```

**Or in Frappe Cloud:**
- Go to **Apps** → **Walue AI** → **Update**

### Updating the App

When you push changes to GitHub:

1. Commit your changes locally
2. Push to GitHub: `git push origin main`
3. In Frappe Cloud:
   - **Apps** → **Walue AI** → **Update**
   - Or enable auto-updates in app settings

### Development Workflow

**Recommended Flow:**

1. **Local Development**:
   ```bash
   # Make changes locally
   cd frappe-bench/apps/walue_ai
   # Edit files
   git commit -am "Update feature"
   git push origin main
   ```

2. **Test on Staging**:
   - Deploy to a test Frappe Cloud site first
   - Verify changes work correctly

3. **Deploy to Production**:
   - Update the production site via Frappe Cloud dashboard

### Security Best Practices

1. **Never commit sensitive data** to GitHub
2. **Use environment variables** for API keys
3. **Enable SSL** (automatic on Frappe Cloud)
4. **Regular backups** (automatic on Frappe Cloud)
5. **Monitor error logs** regularly

### Support Resources

- **Frappe Cloud Docs**: https://frappecloud.com/docs
- **Frappe Forum**: https://discuss.frappe.io
- **GitHub Issues**: https://github.com/chinmaybhatk/walue_ai/issues

### Cost Estimation

**Frappe Cloud Pricing** (as of 2025):
- Starter: ~$10-30/month
- Business: ~$50-100/month
- Custom: Contact sales

Plans include:
- Hosting
- Automatic backups
- SSL certificates
- Email sending
- Support

---

## Next Steps

After deployment:

1. ✅ Test the landing page
2. ✅ Configure custom domain
3. ✅ Customize branding
4. ✅ Add your content
5. ✅ Set up analytics
6. ✅ Launch! 🚀

**Your site is now live at**: `https://yoursite.frappe.cloud/home`

Need help? Open an issue: https://github.com/chinmaybhatk/walue_ai/issues
#!/usr/bin/env python3
"""
SAS IDeaS Enterprise MCP Dashboard UI Templates
==============================================
Modern, responsive management console with Tailwind CSS, KPI cards,
live domain kill-switches, API key generator, and real-time audit logs.
"""

from typing import Any, Dict, List


def render_login_page(error: str = None) -> str:
    err_html = f"""
    <div class="mb-4 bg-red-900/40 border border-red-500/50 text-red-200 px-4 py-3 rounded-lg text-sm flex items-center gap-2">
        <svg class="w-5 h-5 text-red-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        <span>{error}</span>
    </div>
    """ if error else ""

    return f"""<!DOCTYPE html>
<html lang="en" class="h-full bg-slate-950 text-slate-100">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAS IDeaS MCP Console - Login</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>body {{ font-family: 'Inter', sans-serif; }}</style>
</head>
<body class="h-full flex items-center justify-center p-4 bg-gradient-to-br from-slate-950 via-slate-900 to-indigo-950">
    <div class="w-full max-w-md">
        <div class="text-center mb-8">
            <div class="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-indigo-600/20 border border-indigo-500/30 text-indigo-400 mb-4 shadow-lg shadow-indigo-500/10">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
            </div>
            <h1 class="text-2xl font-bold tracking-tight text-white">IDeaS Enterprise MCP</h1>
            <p class="text-sm text-slate-400 mt-1">Master Operations & Copilot Management Console</p>
        </div>

        <div class="bg-slate-900/80 border border-slate-800 backdrop-blur-xl rounded-2xl p-8 shadow-2xl">
            {err_html}
            <form method="POST" action="/admin/login" class="space-y-5">
                <div>
                    <label class="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">Username</label>
                    <input type="text" name="username" required autofocus placeholder="admin"
                        class="w-full px-4 py-2.5 rounded-lg bg-slate-950/70 border border-slate-800 text-white placeholder-slate-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition">
                </div>
                <div>
                    <label class="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">Password</label>
                    <input type="password" name="password" required placeholder="••••••••••••"
                        class="w-full px-4 py-2.5 rounded-lg bg-slate-950/70 border border-slate-800 text-white placeholder-slate-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition">
                </div>
                <button type="submit"
                    class="w-full py-3 px-4 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-medium shadow-lg shadow-indigo-600/25 transition duration-150 ease-in-out">
                    Sign in to Console
                </button>
            </form>
        </div>
        <p class="text-center text-xs text-slate-600 mt-6">SAS IDeaS Revenue Solutions &copy; 2026</p>
    </div>
    <script>
      const path = window.location.pathname;
      const prefixMatch = path.match(/^(.*?)[/]admin([/].*)?$/);
      if (prefixMatch && prefixMatch[1]) {{
        const p = prefixMatch[1];
        document.querySelectorAll('form').forEach(f => {{
          const act = f.getAttribute('action');
          if (act && act.startsWith('/admin')) {{ f.action = p + act; }}
        }});
      }}
    </script>
</body>
</html>"""


def render_dashboard(data: Dict[str, Any], new_key: str = None) -> str:
    keys = data.get("keys", [])
    domains = data.get("domains", [])
    recent_logs = data.get("recent_logs", [])
    total_calls = data.get("total_calls", 0)
    calls_24h = data.get("calls_24h", 0)
    avg_latency = data.get("avg_latency_ms", 0.0)
    success_rate = data.get("success_rate", 100.0)
    error_count = data.get("error_count", 0)

    # Generate new key alert banner
    new_key_banner = ""
    if new_key:
        new_key_banner = f"""
        <div class="mb-8 p-4 bg-emerald-950/60 border border-emerald-500/50 rounded-xl text-emerald-200 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <span class="p-2 rounded-lg bg-emerald-500/20 text-emerald-400">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                </span>
                <div>
                    <h4 class="font-semibold text-white">New API Key Generated Successfully</h4>
                    <p class="text-xs text-emerald-300/80">Copy this key now. For security, full keys are only displayed at creation.</p>
                </div>
            </div>
            <div class="flex items-center gap-2 w-full md:w-auto">
                <code class="px-3 py-1.5 rounded-lg bg-slate-900 border border-emerald-500/30 text-emerald-400 font-mono text-xs select-all flex-1 md:flex-none">{new_key}</code>
                <button onclick="navigator.clipboard.writeText('{new_key}'); alert('API Key copied to clipboard!');" 
                    class="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold rounded-lg shadow transition">
                    Copy Key
                </button>
            </div>
        </div>
        """

    # Domain rows
    domain_rows = ""
    for d in domains:
        is_en = bool(d["is_enabled"])
        status_badge = '<span class="px-2 py-0.5 text-xs font-semibold rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Active</span>' if is_en else '<span class="px-2 py-0.5 text-xs font-semibold rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20">Disabled</span>'
        btn_action = "Disable" if is_en else "Enable"
        btn_class = "bg-amber-600/20 text-amber-300 hover:bg-amber-600/30 border-amber-500/30" if is_en else "bg-emerald-600/20 text-emerald-300 hover:bg-emerald-600/30 border-emerald-500/30"

        domain_rows += f"""
        <tr class="border-b border-slate-800/60 hover:bg-slate-800/20 transition">
            <td class="py-3.5 px-4">
                <div class="font-medium text-white text-sm">{d["display_name"]}</div>
                <div class="text-xs text-slate-500">{d.get("description", "")}</div>
            </td>
            <td class="py-3.5 px-4 text-xs font-mono text-slate-400">{d["tool_count"]} canonical tools</td>
            <td class="py-3.5 px-4">{status_badge}</td>
            <td class="py-3.5 px-4 text-right">
                <form method="POST" action="/admin/domains/toggle" class="inline">
                    <input type="hidden" name="domain_name" value="{d['domain_name']}">
                    <button type="submit" class="px-3 py-1 text-xs font-medium rounded-lg border transition {btn_class}">
                        {btn_action}
                    </button>
                </form>
            </td>
        </tr>
        """

    # API Key rows
    key_rows = ""
    for k in keys:
        is_act = bool(k["is_active"])
        status_badge = '<span class="px-2 py-0.5 text-xs font-semibold rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Active</span>' if is_act else '<span class="px-2 py-0.5 text-xs font-semibold rounded-full bg-rose-500/10 text-rose-400 border border-rose-500/20">Revoked</span>'
        toggle_label = "Revoke" if is_act else "Activate"
        toggle_class = "text-rose-400 hover:text-rose-300 hover:bg-rose-500/10" if is_act else "text-emerald-400 hover:text-emerald-300 hover:bg-emerald-500/10"
        masked_val = k["key_value"][:12] + "••••••••" + k["key_value"][-4:]
        last_used = k.get("last_used_at")
        last_used_display = (last_used[:19].replace("T", " ")) if last_used else "Never"
        rpm = k.get("rate_limit_rpm", 0)
        rpm_badge = '<span class="px-2 py-0.5 text-xs font-semibold rounded bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Unlimited (&infin;)</span>' if (rpm is None or rpm <= 0) else f'<span class="font-mono text-xs text-slate-300">{rpm} / min</span>'
        rpm_val = 0 if (rpm is None or rpm <= 0) else rpm

        key_rows += f"""
        <tr class="border-b border-slate-800/60 hover:bg-slate-800/20 transition">
            <td class="py-3.5 px-4">
                <div class="font-medium text-white text-sm">{k["client_name"]}</div>
                <div class="text-xs text-slate-500">{k.get("description", "No description")}</div>
            </td>
            <td class="py-3.5 px-4">
                <div class="flex items-center gap-2">
                    <code class="font-mono text-xs text-indigo-300 bg-slate-950 px-2 py-1 rounded border border-slate-800">{masked_val}</code>
                    <button onclick="navigator.clipboard.writeText('{k['key_value']}'); alert('Full API key copied!');" title="Copy Key" class="text-slate-400 hover:text-white transition">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
                    </button>
                </div>
            </td>
            <td class="py-3.5 px-4">
                <div class="flex items-center gap-2">
                    {rpm_badge}
                    <form method="POST" action="/admin/keys/update-limit" class="inline flex items-center gap-1">
                        <input type="hidden" name="key_id" value="{k['id']}">
                        <input type="number" name="rate_limit_rpm" value="{rpm_val}" min="0" max="10000" title="Set to 0 for Unlimited"
                            class="w-16 px-1.5 py-0.5 text-xs bg-slate-950/80 border border-slate-700 rounded text-white text-center focus:outline-none focus:ring-1 focus:ring-indigo-500">
                        <button type="submit" class="text-[10px] uppercase font-bold text-indigo-400 hover:text-indigo-300 px-1.5 py-0.5 rounded bg-slate-800 hover:bg-slate-700 transition" title="Save Limit (0 = Unlimited)">
                            Set
                        </button>
                    </form>
                </div>
            </td>
            <td class="py-3.5 px-4 text-xs font-semibold text-slate-300">{k.get("total_calls", 0):,}</td>
            <td class="py-3.5 px-4 text-xs text-slate-400">{last_used_display}</td>
            <td class="py-3.5 px-4">{status_badge}</td>
            <td class="py-3.5 px-4 text-right">
                <form method="POST" action="/admin/keys/toggle" class="inline mr-2">
                    <input type="hidden" name="key_id" value="{k['id']}">
                    <button type="submit" class="px-2.5 py-1 text-xs font-medium rounded-lg border border-slate-700 transition {toggle_class}">
                        {toggle_label}
                    </button>
                </form>
                <form method="POST" action="/admin/keys/delete" class="inline" onsubmit="return confirm('Permanently delete API key for {k['client_name']}?');">
                    <input type="hidden" name="key_id" value="{k['id']}">
                    <button type="submit" class="text-slate-500 hover:text-rose-400 p-1 rounded transition" title="Delete Key">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                    </button>
                </form>
            </td>
        </tr>
        """

    # Audit log rows
    log_rows = ""
    for log in recent_logs:
        code = log["status_code"]
        code_badge = '<span class="text-emerald-400 font-mono font-semibold">200</span>' if code < 400 else f'<span class="text-rose-400 font-mono font-semibold">{code}</span>'
        tool_name = log.get("tool_name") or log.get("endpoint", "")
        domain = log.get("domain") or "-"
        domain_badge = f'<span class="px-2 py-0.5 text-xs font-medium rounded bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">{domain.upper()}</span>' if domain != "-" else '<span class="text-slate-500">-</span>'
        ts = log.get("timestamp")
        ts_display = (ts[:19].replace("T", " ")) if ts else "-"

        log_rows += f"""
        <tr class="border-b border-slate-800/40 hover:bg-slate-800/10 transition text-xs">
            <td class="py-2.5 px-4 font-mono text-slate-400">{ts_display}</td>
            <td class="py-2.5 px-4 font-medium text-slate-200">{log["client_name"]}</td>
            <td class="py-2.5 px-4">{domain_badge}</td>
            <td class="py-2.5 px-4 font-mono text-slate-300">{tool_name}</td>
            <td class="py-2.5 px-4">{code_badge}</td>
            <td class="py-2.5 px-4 font-mono text-slate-400">{log["execution_time_ms"]} ms</td>
            <td class="py-2.5 px-4 font-mono text-slate-500">{log.get("client_ip", "")}</td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html lang="en" class="h-full bg-slate-950 text-slate-100">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAS IDeaS Enterprise MCP Console</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; }}
        code, .font-mono {{ font-family: 'JetBrains Mono', monospace; }}
    </style>
</head>
<body class="min-h-full bg-slate-950 text-slate-100 antialiased">
    <!-- Navigation Header -->
    <header class="border-b border-slate-800 bg-slate-900/60 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl bg-indigo-600 flex items-center justify-center text-white font-bold shadow-md shadow-indigo-600/30">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                </div>
                <div>
                    <span class="font-bold text-base text-white tracking-tight">SAS IDeaS Enterprise MCP</span>
                    <span class="ml-2 px-2 py-0.5 text-xs font-semibold rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">Production v2.0</span>
                </div>
            </div>
            <div class="flex items-center gap-4">
                <a href="/admin/logs/export" class="text-xs font-medium text-slate-400 hover:text-white px-3 py-1.5 rounded-lg border border-slate-800 hover:bg-slate-800 transition flex items-center gap-1.5">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                    Export Audit CSV
                </a>
                <a href="/admin/logout" class="text-xs font-medium text-rose-400 hover:text-rose-300 px-3 py-1.5 rounded-lg border border-rose-900/40 hover:bg-rose-950/40 transition">
                    Sign Out
                </a>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {new_key_banner}

        <!-- KPI Metrics Overview -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-5 mb-8">
            <div class="bg-slate-900/60 border border-slate-800 p-5 rounded-2xl">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold uppercase tracking-wider text-slate-400">Total Tool Calls</span>
                    <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">All-Time</span>
                </div>
                <div class="mt-2 text-3xl font-bold text-white tracking-tight">{total_calls:,}</div>
                <div class="mt-1 text-xs text-slate-500">+{calls_24h:,} in the last 24 hours</div>
            </div>

            <div class="bg-slate-900/60 border border-slate-800 p-5 rounded-2xl">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold uppercase tracking-wider text-slate-400">Active API Keys</span>
                    <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Authorized</span>
                </div>
                <div class="mt-2 text-3xl font-bold text-emerald-400 tracking-tight">{len(keys)}</div>
                <div class="mt-1 text-xs text-slate-500">Client credentials provisioned</div>
            </div>

            <div class="bg-slate-900/60 border border-slate-800 p-5 rounded-2xl">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold uppercase tracking-wider text-slate-400">Average Latency</span>
                    <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-blue-500/10 text-blue-400 border border-blue-500/20">End-to-End</span>
                </div>
                <div class="mt-2 text-3xl font-bold text-white tracking-tight">{avg_latency} ms</div>
                <div class="mt-1 text-xs text-slate-500">FastAPI + Async JSON-RPC</div>
            </div>

            <div class="bg-slate-900/60 border border-slate-800 p-5 rounded-2xl">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold uppercase tracking-wider text-slate-400">Success Rate</span>
                    <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Reliability</span>
                </div>
                <div class="mt-2 text-3xl font-bold text-emerald-400 tracking-tight">{success_rate}%</div>
                <div class="mt-1 text-xs text-slate-500">{error_count} blocked / failed executions</div>
            </div>
        </div>

        <!-- Two Column Layout: Domain Governance & Create API Key -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8">
            <!-- Domain Governance Panel -->
            <div class="lg:col-span-2 bg-slate-900/60 border border-slate-800 rounded-2xl overflow-hidden">
                <div class="p-5 border-b border-slate-800 flex items-center justify-between">
                    <div>
                        <h3 class="font-semibold text-white">Enterprise Domain Governance</h3>
                        <p class="text-xs text-slate-400 mt-0.5">Toggle operational subsystems and inspect tool quotas.</p>
                    </div>
                    <span class="text-xs font-mono text-slate-500">168 Total Tools</span>
                </div>
                <div class="overflow-x-auto">
                    <table class="w-full text-left">
                        <thead>
                            <tr class="text-[11px] font-semibold uppercase tracking-wider text-slate-400 bg-slate-900/40 border-b border-slate-800">
                                <th class="py-3 px-4">Domain System</th>
                                <th class="py-3 px-4">Tool Count</th>
                                <th class="py-3 px-4">Status</th>
                                <th class="py-3 px-4 text-right">Kill Switch</th>
                            </tr>
                        </thead>
                        <tbody>
                            {domain_rows}
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Create New API Key Card -->
            <div class="bg-slate-900/60 border border-slate-800 rounded-2xl p-6">
                <h3 class="font-semibold text-white">Issue Client API Key</h3>
                <p class="text-xs text-slate-400 mt-1 mb-5">Provision authenticated credentials for Microsoft Copilot Studio or agents.</p>

                <form method="POST" action="/admin/keys/create" class="space-y-4">
                    <div>
                        <label class="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-1.5">Client / Agent Name</label>
                        <input type="text" name="client_name" required placeholder="e.g. M365_Copilot_Prod"
                            class="w-full px-3.5 py-2 rounded-lg bg-slate-950/80 border border-slate-800 text-white placeholder-slate-600 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 transition">
                    </div>
                    <div>
                        <label class="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-1.5">Description (Optional)</label>
                        <input type="text" name="description" placeholder="e.g. Triage agent in Teams"
                            class="w-full px-3.5 py-2 rounded-lg bg-slate-950/80 border border-slate-800 text-white placeholder-slate-600 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 transition">
                    </div>
                    <div>
                        <label class="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-1.5">Rate Limit (Requests / Min, 0 = Unlimited)</label>
                        <input type="number" name="rate_limit_rpm" value="0" min="0" max="10000"
                            class="w-full px-3.5 py-2 rounded-lg bg-slate-950/80 border border-slate-800 text-white text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 transition">
                    </div>
                    <button type="submit"
                        class="w-full mt-2 py-2.5 px-4 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold shadow-md shadow-indigo-600/25 transition">
                        Generate & Authorize Key
                    </button>
                </form>
            </div>
        </div>

        <!-- API Key Management Table -->
        <div class="bg-slate-900/60 border border-slate-800 rounded-2xl mb-8 overflow-hidden">
            <div class="p-5 border-b border-slate-800 flex items-center justify-between">
                <div>
                    <h3 class="font-semibold text-white">Authorized API Keys</h3>
                    <p class="text-xs text-slate-400 mt-0.5">Manage access tokens, revocation, and per-client usage tracking.</p>
                </div>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left">
                    <thead>
                        <tr class="text-[11px] font-semibold uppercase tracking-wider text-slate-400 bg-slate-900/40 border-b border-slate-800">
                            <th class="py-3 px-4">Client Name</th>
                            <th class="py-3 px-4">API Key Token</th>
                            <th class="py-3 px-4">Rate Limit</th>
                            <th class="py-3 px-4">Invocations</th>
                            <th class="py-3 px-4">Last Activity</th>
                            <th class="py-3 px-4">Status</th>
                            <th class="py-3 px-4 text-right">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {key_rows}
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Real-Time Audit Log Table -->
        <div class="bg-slate-900/60 border border-slate-800 rounded-2xl overflow-hidden">
            <div class="p-5 border-b border-slate-800 flex items-center justify-between">
                <div>
                    <h3 class="font-semibold text-white">Real-Time Triage & Tool Execution Log</h3>
                    <p class="text-xs text-slate-400 mt-0.5">Recent diagnostic tool invocations by Copilot agents and engineers.</p>
                </div>
                <span class="text-xs font-mono text-slate-500">Showing last 50 events</span>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left">
                    <thead>
                        <tr class="text-[11px] font-semibold uppercase tracking-wider text-slate-400 bg-slate-900/40 border-b border-slate-800">
                            <th class="py-2.5 px-4">Timestamp (UTC)</th>
                            <th class="py-2.5 px-4">Client</th>
                            <th class="py-2.5 px-4">Domain</th>
                            <th class="py-2.5 px-4">Tool / Endpoint</th>
                            <th class="py-2.5 px-4">Status</th>
                            <th class="py-2.5 px-4">Duration</th>
                            <th class="py-2.5 px-4">Source IP</th>
                        </tr>
                    </thead>
                    <tbody>
                        {log_rows if log_rows else '<tr><td colspan="7" class="text-center py-8 text-slate-500 text-sm">No tool invocations recorded yet.</td></tr>'}
                    </tbody>
                </table>
            </div>
        </div>
    </main>
    <script>
      const path = window.location.pathname;
      const prefixMatch = path.match(/^(.*?)[/]admin([/].*)?$/);
      if (prefixMatch && prefixMatch[1]) {{
        const p = prefixMatch[1];
        document.querySelectorAll('form').forEach(f => {{
          const act = f.getAttribute('action');
          if (act && act.startsWith('/admin')) {{ f.action = p + act; }}
        }});
        document.querySelectorAll('a').forEach(a => {{
          const href = a.getAttribute('href');
          if (href && href.startsWith('/admin')) {{ a.href = p + href; }}
        }});
      }}
    </script>
</body>
</html>"""

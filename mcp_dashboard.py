#!/usr/bin/env python3
"""
SAS IDeaS Enterprise MCP Dashboard UI Templates
==============================================
Modern, highly detailed management console with Tailwind CSS, KPI cards,
subsystem topology health grid, 185-tool directory explorer, top tool analytics,
domain kill-switches, API key generator, and real-time audit log inspector.
"""

import json
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
    top_tools = data.get("top_tools", [])
    status_breakdown = data.get("status_breakdown", {})
    all_tools = data.get("all_tools", [])
    total_tools_count = data.get("total_tools_count", len(all_tools) or 185)
    domain_counts = data.get("domain_counts", {})

    # Generate new key alert banner
    new_key_banner = ""
    if new_key:
        new_key_banner = f"""
        <div class="mb-8 p-4 bg-emerald-950/60 border border-emerald-500/50 rounded-xl text-emerald-200 flex flex-col md:flex-row items-start md:items-center justify-between gap-4 shadow-lg shadow-emerald-950/40">
            <div class="flex items-center gap-3">
                <span class="p-2 rounded-lg bg-emerald-500/20 text-emerald-400">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                </span>
                <div>
                    <h4 class="font-semibold text-white">New API Key Generated Successfully</h4>
                    <p class="text-xs text-emerald-300/80">Copy this token now. For security reasons, full token values are only revealed at generation time.</p>
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

    # Domain rows for Governance
    domain_rows = ""
    domain_colors = {
        "cma": "text-purple-400 border-purple-500/20 bg-purple-500/10",
        "optix": "text-cyan-400 border-cyan-500/20 bg-cyan-500/10",
        "ups_fds": "text-blue-400 border-blue-500/20 bg-blue-500/10",
        "datadog": "text-pink-400 border-pink-500/20 bg-pink-500/10",
        "confluence": "text-emerald-400 border-emerald-500/20 bg-emerald-500/10",
        "salesforce": "text-amber-400 border-amber-500/20 bg-amber-500/10",
    }
    for d in domains:
        d_name = d["domain_name"].lower()
        is_en = bool(d["is_enabled"])
        status_badge = '<span class="px-2.5 py-0.5 text-xs font-semibold rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Operational</span>' if is_en else '<span class="px-2.5 py-0.5 text-xs font-semibold rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20">Disabled</span>'
        btn_action = "Disable" if is_en else "Enable"
        btn_class = "bg-amber-600/20 text-amber-300 hover:bg-amber-600/30 border-amber-500/30" if is_en else "bg-emerald-600/20 text-emerald-300 hover:bg-emerald-600/30 border-emerald-500/30"
        color_class = domain_colors.get(d_name, "text-slate-300 border-slate-700 bg-slate-800/40")

        domain_rows += f"""
        <tr class="border-b border-slate-800/60 hover:bg-slate-800/20 transition">
            <td class="py-3.5 px-4">
                <div class="flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
                    <span class="font-semibold text-white text-sm">{d["display_name"]}</span>
                    <span class="text-[10px] uppercase font-mono px-2 py-0.5 rounded border {color_class}">{d_name}</span>
                </div>
                <div class="text-xs text-slate-500 mt-0.5">{d.get("description", "")}</div>
            </td>
            <td class="py-3.5 px-4 text-xs font-mono font-medium text-slate-300">{d["tool_count"]} canonical tools</td>
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
                    <code class="font-mono text-xs text-indigo-300 bg-slate-950 px-2.5 py-1 rounded border border-slate-800">{masked_val}</code>
                    <button onclick="navigator.clipboard.writeText('{k['key_value']}'); alert('Full API key copied!');" title="Copy Key" class="text-slate-400 hover:text-white transition p-1">
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

    # Top 10 Tools Rows
    top_tool_rows = ""
    for idx, t in enumerate(top_tools, 1):
        errs = t.get("errors", 0)
        c_cnt = t.get("call_count", 0)
        err_badge = f'<span class="text-rose-400 font-mono text-xs">{errs}</span>' if errs > 0 else '<span class="text-emerald-400 font-mono text-xs">0</span>'
        d_color = domain_colors.get((t.get("domain") or "").lower(), "text-slate-400 border-slate-700 bg-slate-800")
        top_tool_rows += f"""
        <tr class="border-b border-slate-800/40 hover:bg-slate-800/20 text-xs transition">
            <td class="py-2.5 px-3 font-mono text-slate-500 font-bold">#{idx}</td>
            <td class="py-2.5 px-3 font-mono font-medium text-indigo-300 flex items-center gap-1.5">
                <span>{t['tool_name']}</span>
            </td>
            <td class="py-2.5 px-3"><span class="px-2 py-0.5 text-[10px] uppercase font-mono rounded border {d_color}">{t.get('domain', '-')}</span></td>
            <td class="py-2.5 px-3 font-bold text-white text-right">{c_cnt:,}</td>
            <td class="py-2.5 px-3 font-mono text-slate-300 text-right">{t.get('avg_ms', 0)} ms</td>
            <td class="py-2.5 px-3 text-right">{err_badge}</td>
        </tr>
        """
    if not top_tool_rows:
        top_tool_rows = '<tr><td colspan="6" class="text-center py-6 text-slate-500 text-xs">No tool invocations logged yet.</td></tr>'

    # Audit log rows
    log_rows = ""
    for log in recent_logs:
        code = log["status_code"]
        code_badge = '<span class="text-emerald-400 font-mono font-bold">200 OK</span>' if code < 400 else f'<span class="text-rose-400 font-mono font-bold">{code}</span>'
        tool_name = log.get("tool_name") or log.get("endpoint", "")
        domain = log.get("domain") or "-"
        domain_badge = f'<span class="px-2 py-0.5 text-[10px] font-mono rounded border {domain_colors.get(domain.lower(), "text-slate-400 border-slate-700 bg-slate-800")}">{domain.upper()}</span>' if domain != "-" else '<span class="text-slate-500">-</span>'
        ts = log.get("timestamp")
        ts_display = (ts[:19].replace("T", " ")) if ts else "-"
        duration = log.get("execution_time_ms", 0.0)
        dur_color = "text-emerald-400" if duration < 150 else ("text-cyan-400" if duration < 500 else "text-amber-400")

        log_rows += f"""
        <tr class="border-b border-slate-800/40 hover:bg-slate-800/15 transition text-xs audit-row" data-domain="{domain.lower()}" data-code="{code}">
            <td class="py-2.5 px-4 font-mono text-slate-400">{ts_display}</td>
            <td class="py-2.5 px-4 font-medium text-slate-200">{log["client_name"]}</td>
            <td class="py-2.5 px-4">{domain_badge}</td>
            <td class="py-2.5 px-4 font-mono text-slate-200 font-medium">{tool_name}</td>
            <td class="py-2.5 px-4">{code_badge}</td>
            <td class="py-2.5 px-4 font-mono {dur_color} font-medium">{duration} ms</td>
            <td class="py-2.5 px-4 font-mono text-slate-500">{log.get("client_ip", "")}</td>
        </tr>
        """

    # Serialize all_tools to JSON for client-side instant search
    all_tools_json = json.dumps(all_tools)

    return f"""<!DOCTYPE html>
<html lang="en" class="h-full bg-slate-950 text-slate-100">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAS IDeaS Enterprise MCP Console</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; }}
        code, .font-mono {{ font-family: 'JetBrains Mono', monospace; }}
    </style>
</head>
<body class="min-h-full bg-slate-950 text-slate-100 antialiased">
    <!-- Top Global Header -->
    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50 shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-indigo-600 flex items-center justify-center text-white font-bold shadow-lg shadow-indigo-600/30">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="font-bold text-base text-white tracking-tight">SAS IDeaS Enterprise MCP Console</span>
                        <span class="px-2 py-0.5 text-[10px] font-bold uppercase rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">Production v2.5</span>
                        <span class="px-2 py-0.5 text-[10px] font-bold uppercase rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/30">{total_tools_count} Tools</span>
                    </div>
                    <p class="text-xs text-slate-400 hidden sm:block">Real-time SRE telemetry, domain governance, and multi-system integration hub</p>
                </div>
            </div>

            <!-- Header Quick Action Bar -->
            <div class="flex items-center gap-3">
                <!-- Auto Refresh Toggle -->
                <div class="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-800 text-xs">
                    <span id="refresh-pulse" class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                    <span class="text-slate-400 font-mono text-[11px]" id="refresh-label">Live: <span id="countdown">15</span>s</span>
                    <input type="checkbox" id="autorefresh-toggle" checked class="rounded bg-slate-900 border-slate-700 text-indigo-600 focus:ring-0 cursor-pointer">
                </div>

                <a href="/admin/logs/export" class="text-xs font-medium text-slate-300 hover:text-white px-3 py-1.5 rounded-lg border border-slate-800 hover:bg-slate-800 transition flex items-center gap-1.5">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                    Export CSV
                </a>
                <a href="/admin/logout" class="text-xs font-medium text-rose-400 hover:text-rose-300 px-3 py-1.5 rounded-lg border border-rose-900/40 hover:bg-rose-950/40 transition">
                    Sign Out
                </a>
            </div>
        </div>

        <!-- Quick Jump Links to Enterprise Portals -->
        <div class="bg-slate-950/70 border-t border-slate-800/80 px-4 sm:px-6 lg:px-8 py-2">
            <div class="max-w-7xl mx-auto flex items-center justify-between overflow-x-auto text-xs gap-4 text-slate-400">
                <span class="font-semibold uppercase tracking-wider text-[10px] text-slate-500 shrink-0">Operational Portals:</span>
                <div class="flex items-center gap-4 shrink-0">
                    <a href="https://htng-troubleshooter.ideasrms.com/troubleshootV2/#!Troubleshooting/tId%23choice" target="_blank" class="hover:text-cyan-300 transition flex items-center gap-1">
                        <span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span> HTNG Troubleshooter V2 (Choice) &nearr;
                    </a>
                    <a href="https://integration-setting-internal.ideasrms.com/" target="_blank" class="hover:text-purple-300 transition flex items-center gap-1">
                        <span class="w-1.5 h-1.5 rounded-full bg-purple-400"></span> HAL Explorer (Spring Data REST) &nearr;
                    </a>
                    <a href="https://app.datadoghq.com" target="_blank" class="hover:text-pink-300 transition flex items-center gap-1">
                        <span class="w-1.5 h-1.5 rounded-full bg-pink-400"></span> Datadog Monitors &nearr;
                    </a>
                    <a href="/docs" target="_blank" class="hover:text-emerald-300 transition flex items-center gap-1">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span> OpenAPI Swagger UI &nearr;
                    </a>
                </div>
                <div class="font-mono text-[11px] text-slate-500 hidden md:block">
                    Host: <span class="text-slate-300 font-semibold">sicsappsina6.in.sas.com</span>
                </div>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
        {new_key_banner}

        <!-- 5-Column High Impact KPI Row -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
            <div class="bg-slate-900/60 border border-slate-800 p-4 rounded-2xl">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold uppercase tracking-wider text-slate-400">Total Tool Calls</span>
                    <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">All-Time</span>
                </div>
                <div class="mt-2 text-2xl font-bold text-white tracking-tight">{total_calls:,}</div>
                <div class="mt-1 text-xs text-slate-500">+{calls_24h:,} past 24 hours</div>
            </div>

            <div class="bg-slate-900/60 border border-slate-800 p-4 rounded-2xl">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold uppercase tracking-wider text-slate-400">Success Rate</span>
                    <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Reliability</span>
                </div>
                <div class="mt-2 text-2xl font-bold text-emerald-400 tracking-tight">{success_rate}%</div>
                <div class="mt-1 text-xs text-slate-500">{error_count} blocked / failed</div>
            </div>

            <div class="bg-slate-900/60 border border-slate-800 p-4 rounded-2xl">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold uppercase tracking-wider text-slate-400">Avg Latency</span>
                    <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-blue-500/10 text-blue-400 border border-blue-500/20">E2E</span>
                </div>
                <div class="mt-2 text-2xl font-bold text-white tracking-tight">{avg_latency} ms</div>
                <div class="mt-1 text-xs text-slate-500">FastAPI Async RPC</div>
            </div>

            <div class="bg-slate-900/60 border border-slate-800 p-4 rounded-2xl">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold uppercase tracking-wider text-slate-400">Master Tools</span>
                    <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-purple-500/10 text-purple-400 border border-purple-500/20">Active</span>
                </div>
                <div class="mt-2 text-2xl font-bold text-purple-400 tracking-tight">{total_tools_count}</div>
                <div class="mt-1 text-xs text-slate-500">Across 6 Domains</div>
            </div>

            <div class="bg-slate-900/60 border border-slate-800 p-4 rounded-2xl">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold uppercase tracking-wider text-slate-400">Authorized Keys</span>
                    <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Active</span>
                </div>
                <div class="mt-2 text-2xl font-bold text-white tracking-tight">{len(keys)}</div>
                <div class="mt-1 text-xs text-slate-500">M365 Copilot & Agents</div>
            </div>
        </div>

        <!-- Connected Subsystem Health & Topology Matrix -->
        <div class="bg-slate-900/60 border border-slate-800 rounded-2xl p-6">
            <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 mb-4">
                <div>
                    <h3 class="font-bold text-base text-white flex items-center gap-2">
                        <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                        Connected Subsystems Live Topology
                    </h3>
                    <p class="text-xs text-slate-400">Live operational status across enterprise databases, microservices, and partner gateways.</p>
                </div>
                <span class="text-xs font-mono text-emerald-400 bg-emerald-500/10 border border-emerald-500/30 px-2.5 py-1 rounded-full flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-400"></span> All 9 Connected Systems Healthy
                </span>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
                <!-- Node 1: CMA Edge Gateway -->
                <div class="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800/80 hover:border-purple-500/40 transition">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                            <span class="font-semibold text-white text-xs">CMA Edge Gateway</span>
                        </div>
                        <span class="text-[10px] font-mono text-slate-400">172.27.210.162:8555</span>
                    </div>
                    <div class="text-[11px] text-slate-400 mt-1.5">Spring Batch execution engine (19,496 chains). Deadlock & step history tracking.</div>
                </div>

                <!-- Node 2: Optix DW Cluster -->
                <div class="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800/80 hover:border-cyan-500/40 transition">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                            <span class="font-semibold text-white text-xs">Optix DW MSSQL Cluster</span>
                        </div>
                        <span class="text-[10px] font-mono text-slate-400">PROD_1..6 (1433)</span>
                    </div>
                    <div class="text-[11px] text-slate-400 mt-1.5">3-Node SQL Server cluster storing 420+ tenant DBs. Strict WITH (NOLOCK) read-only.</div>
                </div>

                <!-- Node 3: HAL Explorer & Integration Hub -->
                <div class="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800/80 hover:border-purple-500/40 transition">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                            <span class="font-semibold text-white text-xs">HAL Integration Hub</span>
                        </div>
                        <span class="text-[10px] font-mono text-slate-400">Spring Data REST</span>
                    </div>
                    <div class="text-[11px] text-slate-400 mt-1.5">https://integration-setting-internal.ideasrms.com/ (Vendor & property configs).</div>
                </div>

                <!-- Node 4: UPS / FDS Platform -->
                <div class="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800/80 hover:border-blue-500/40 transition">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                            <span class="font-semibold text-white text-xs">UPS & FDS Platform</span>
                        </div>
                        <span class="text-[10px] font-mono text-slate-400">OAuth2 M2M</span>
                    </div>
                    <div class="text-[11px] text-slate-400 mt-1.5">User permissions, property metadata, geo-radius lookups, and token lifecycle.</div>
                </div>

                <!-- Node 5: Datadog Observability -->
                <div class="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800/80 hover:border-pink-500/40 transition">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                            <span class="font-semibold text-white text-xs">Datadog Telemetry</span>
                        </div>
                        <span class="text-[10px] font-mono text-slate-400">datadoghq.com</span>
                    </div>
                    <div class="text-[11px] text-slate-400 mt-1.5">Inbound PMS Kafka stream traces, decision delivery errors, and alert monitors.</div>
                </div>

                <!-- Node 6: HTNG Troubleshooter V2 -->
                <div class="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800/80 hover:border-cyan-500/40 transition">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                            <span class="font-semibold text-white text-xs">HTNG Troubleshooter V2</span>
                        </div>
                        <span class="text-[10px] font-mono text-slate-400">Vaadin 8 Portal</span>
                    </div>
                    <div class="text-[11px] text-slate-400 mt-1.5">ChoiceAdvantage & CRS 2-way HTNG XML rate & restriction message exchange tracker.</div>
                </div>

                <!-- Node 7: CEDF SFTP Ingestion -->
                <div class="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800/80 hover:border-blue-500/40 transition">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                            <span class="font-semibold text-white text-xs">CEDF SFTP Gateway</span>
                        </div>
                        <span class="text-[10px] font-mono text-slate-400">cedf.ideasrms.com</span>
                    </div>
                    <div class="text-[11px] text-slate-400 mt-1.5">Batch transaction extraction pipeline (`res_*.csv`, `blk_*.csv`) and upload status.</div>
                </div>

                <!-- Node 8: Salesforce Service Cloud -->
                <div class="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800/80 hover:border-amber-500/40 transition">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                            <span class="font-semibold text-white text-xs">Salesforce Service Cloud</span>
                        </div>
                        <span class="text-[10px] font-mono text-slate-400">REST API</span>
                    </div>
                    <div class="text-[11px] text-slate-400 mt-1.5">Precedent cases, engineering escalations, property accounts, and resolution tasks.</div>
                </div>

                <!-- Node 9: Qdrant Vector RAG -->
                <div class="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800/80 hover:border-emerald-500/40 transition">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                            <span class="font-semibold text-white text-xs">Qdrant Vector Engine</span>
                        </div>
                        <span class="text-[10px] font-mono text-slate-400">172.27.210.162:6333</span>
                    </div>
                    <div class="text-[11px] text-slate-400 mt-1.5">Confluence runbook embeddings and G3 domain knowledge similarity search.</div>
                </div>
            </div>
        </div>

        <!-- Two Column Section: Top Tools Leaderboard & Traffic Distribution -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <!-- Top 10 Most Invoked Diagnostic Tools -->
            <div class="lg:col-span-2 bg-slate-900/60 border border-slate-800 rounded-2xl overflow-hidden">
                <div class="p-5 border-b border-slate-800 flex items-center justify-between">
                    <div>
                        <h3 class="font-semibold text-white flex items-center gap-2">
                            <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
                            Top Diagnostic Tools Leaderboard
                        </h3>
                        <p class="text-xs text-slate-400 mt-0.5">Most frequently executed tools across SRE investigations.</p>
                    </div>
                    <span class="text-xs font-mono text-slate-500">Live Telemetry</span>
                </div>
                <div class="overflow-x-auto">
                    <table class="w-full text-left">
                        <thead>
                            <tr class="text-[11px] font-semibold uppercase tracking-wider text-slate-400 bg-slate-900/40 border-b border-slate-800">
                                <th class="py-2.5 px-3">Rank</th>
                                <th class="py-2.5 px-3">Tool Name</th>
                                <th class="py-2.5 px-3">Domain</th>
                                <th class="py-2.5 px-3 text-right">Calls</th>
                                <th class="py-2.5 px-3 text-right">Avg Latency</th>
                                <th class="py-2.5 px-3 text-right">Errors</th>
                            </tr>
                        </thead>
                        <tbody>
                            {top_tool_rows}
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- HTTP Status & Domain Breakdown -->
            <div class="bg-slate-900/60 border border-slate-800 rounded-2xl p-5 flex flex-col justify-between">
                <div>
                    <h3 class="font-semibold text-white flex items-center gap-2">
                        <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z"/></svg>
                        Traffic & Response Matrix
                    </h3>
                    <p class="text-xs text-slate-400 mt-0.5">HTTP response code breakdown.</p>

                    <!-- Status Badges -->
                    <div class="grid grid-cols-2 gap-2 mt-4">
                        <div class="p-2.5 rounded-lg bg-emerald-950/30 border border-emerald-500/20 flex items-center justify-between">
                            <span class="text-xs font-semibold text-emerald-400">200 OK</span>
                            <span class="font-mono text-sm font-bold text-white">{status_breakdown.get('ok_200', total_calls - error_count):,}</span>
                        </div>
                        <div class="p-2.5 rounded-lg bg-blue-950/30 border border-blue-500/20 flex items-center justify-between">
                            <span class="text-xs font-semibold text-blue-400">401 Auth</span>
                            <span class="font-mono text-sm font-bold text-white">{status_breakdown.get('err_401', 0):,}</span>
                        </div>
                        <div class="p-2.5 rounded-lg bg-amber-950/30 border border-amber-500/20 flex items-center justify-between">
                            <span class="text-xs font-semibold text-amber-400">429 Throttled</span>
                            <span class="font-mono text-sm font-bold text-white">{status_breakdown.get('err_429', 0):,}</span>
                        </div>
                        <div class="p-2.5 rounded-lg bg-rose-950/30 border border-rose-500/20 flex items-center justify-between">
                            <span class="text-xs font-semibold text-rose-400">5xx Server Err</span>
                            <span class="font-mono text-sm font-bold text-white">{status_breakdown.get('err_500', error_count):,}</span>
                        </div>
                    </div>

                    <!-- Domain Invocations Distribution -->
                    <h4 class="text-xs font-semibold uppercase tracking-wider text-slate-400 mt-6 mb-3">Domain Activity Share</h4>
                    <div class="space-y-2 text-xs">
                        <div>
                            <div class="flex justify-between text-slate-300 mb-1">
                                <span>CMA Batch & SQL Gateway</span>
                                <span class="font-mono text-slate-400">{domain_counts.get('cma', 0)} calls</span>
                            </div>
                            <div class="w-full h-1.5 rounded-full bg-slate-800 overflow-hidden">
                                <div class="h-full bg-purple-500 rounded-full" style="width: {min(100, int(domain_counts.get('cma', 0) / max(1, total_calls) * 100))}%"></div>
                            </div>
                        </div>
                        <div>
                            <div class="flex justify-between text-slate-300 mb-1">
                                <span>Optix Data Warehouse</span>
                                <span class="font-mono text-slate-400">{domain_counts.get('optix', 0)} calls</span>
                            </div>
                            <div class="w-full h-1.5 rounded-full bg-slate-800 overflow-hidden">
                                <div class="h-full bg-cyan-500 rounded-full" style="width: {min(100, int(domain_counts.get('optix', 0) / max(1, total_calls) * 100))}%"></div>
                            </div>
                        </div>
                        <div>
                            <div class="flex justify-between text-slate-300 mb-1">
                                <span>UPS / FDS & HAL Settings</span>
                                <span class="font-mono text-slate-400">{domain_counts.get('ups_fds', 0)} calls</span>
                            </div>
                            <div class="w-full h-1.5 rounded-full bg-slate-800 overflow-hidden">
                                <div class="h-full bg-blue-500 rounded-full" style="width: {min(100, int(domain_counts.get('ups_fds', 0) / max(1, total_calls) * 100))}%"></div>
                            </div>
                        </div>
                        <div>
                            <div class="flex justify-between text-slate-300 mb-1">
                                <span>Datadog Telemetry</span>
                                <span class="font-mono text-slate-400">{domain_counts.get('datadog', 0)} calls</span>
                            </div>
                            <div class="w-full h-1.5 rounded-full bg-slate-800 overflow-hidden">
                                <div class="h-full bg-pink-500 rounded-full" style="width: {min(100, int(domain_counts.get('datadog', 0) / max(1, total_calls) * 100))}%"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="mt-6 pt-4 border-t border-slate-800 text-center">
                    <span class="text-[11px] text-slate-500">Security Guardrail: Strict READ-ONLY Enforcement Active</span>
                </div>
            </div>
        </div>

        <!-- Master 185 Canonical Tool Directory Explorer -->
        <div class="bg-slate-900/60 border border-slate-800 rounded-2xl overflow-hidden">
            <div class="p-5 border-b border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                <div>
                    <h3 class="font-bold text-base text-white flex items-center gap-2">
                        <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                        Canonical Tool Directory & Schema Explorer
                    </h3>
                    <p class="text-xs text-slate-400 mt-0.5">Explore all {total_tools_count} canonical diagnostic tools available to Copilot Studio agents.</p>
                </div>
                <!-- Search Box -->
                <div class="w-full sm:w-80">
                    <div class="relative">
                        <input type="text" id="tool-search" placeholder="Filter tools by name, parameter, or keyword..." 
                            class="w-full px-3.5 py-2 pl-9 rounded-lg bg-slate-950 border border-slate-800 text-white placeholder-slate-600 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500 transition">
                        <svg class="w-4 h-4 text-slate-500 absolute left-2.5 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                    </div>
                </div>
            </div>

            <!-- Domain Filter Buttons -->
            <div class="px-5 py-2.5 bg-slate-950/60 border-b border-slate-800/60 flex items-center gap-2 overflow-x-auto text-xs">
                <button onclick="filterToolsByDomain('all')" class="tool-filter-btn px-2.5 py-1 rounded-md font-semibold text-white bg-indigo-600 transition" data-domain="all">All ({total_tools_count})</button>
                <button onclick="filterToolsByDomain('cma')" class="tool-filter-btn px-2.5 py-1 rounded-md font-medium text-slate-400 hover:text-white hover:bg-slate-800 transition" data-domain="cma">CMA (34)</button>
                <button onclick="filterToolsByDomain('optix')" class="tool-filter-btn px-2.5 py-1 rounded-md font-medium text-slate-400 hover:text-white hover:bg-slate-800 transition" data-domain="optix">Optix (32)</button>
                <button onclick="filterToolsByDomain('ups_fds')" class="tool-filter-btn px-2.5 py-1 rounded-md font-medium text-slate-400 hover:text-white hover:bg-slate-800 transition" data-domain="ups_fds">UPS, FDS & HAL (36)</button>
                <button onclick="filterToolsByDomain('datadog')" class="tool-filter-btn px-2.5 py-1 rounded-md font-medium text-slate-400 hover:text-white hover:bg-slate-800 transition" data-domain="datadog">Datadog (22)</button>
                <button onclick="filterToolsByDomain('confluence')" class="tool-filter-btn px-2.5 py-1 rounded-md font-medium text-slate-400 hover:text-white hover:bg-slate-800 transition" data-domain="confluence">Confluence (32)</button>
                <button onclick="filterToolsByDomain('salesforce')" class="tool-filter-btn px-2.5 py-1 rounded-md font-medium text-slate-400 hover:text-white hover:bg-slate-800 transition" data-domain="salesforce">Salesforce (29)</button>
            </div>

            <!-- Tool Cards Grid -->
            <div id="tool-cards-container" class="p-5 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 max-h-[500px] overflow-y-auto">
                <!-- Dynamically populated via JS -->
            </div>
        </div>

        <!-- Two Column Layout: Domain Governance & Create API Key -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <!-- Domain Governance Panel -->
            <div class="lg:col-span-2 bg-slate-900/60 border border-slate-800 rounded-2xl overflow-hidden">
                <div class="p-5 border-b border-slate-800 flex items-center justify-between">
                    <div>
                        <h3 class="font-semibold text-white">Enterprise Domain Governance</h3>
                        <p class="text-xs text-slate-400 mt-0.5">Toggle operational subsystems and inspect tool quotas.</p>
                    </div>
                    <span class="text-xs font-mono text-slate-500">6 Clusters</span>
                </div>
                <div class="overflow-x-auto">
                    <table class="w-full text-left">
                        <thead>
                            <tr class="text-[11px] font-semibold uppercase tracking-wider text-slate-400 bg-slate-900/40 border-b border-slate-800">
                                <th class="py-3 px-4">Domain Subsystem</th>
                                <th class="py-3 px-4">Canonical Tools</th>
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
        <div class="bg-slate-900/60 border border-slate-800 rounded-2xl overflow-hidden">
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

        <!-- Real-Time Audit Log Table with Filter Controls -->
        <div class="bg-slate-900/60 border border-slate-800 rounded-2xl overflow-hidden">
            <div class="p-5 border-b border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                <div>
                    <h3 class="font-semibold text-white flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                        Real-Time Triage & Execution Audit Log
                    </h3>
                    <p class="text-xs text-slate-400 mt-0.5">Recent diagnostic tool invocations by Copilot agents and engineers.</p>
                </div>
                <!-- Filter Status Options -->
                <div class="flex items-center gap-2 text-xs">
                    <span class="text-slate-500 font-semibold uppercase text-[10px]">Filter Status:</span>
                    <button onclick="filterAuditLogs('all')" class="log-filter-btn px-2.5 py-1 rounded bg-indigo-600 text-white font-medium" data-filter="all">All ({len(recent_logs)})</button>
                    <button onclick="filterAuditLogs('success')" class="log-filter-btn px-2.5 py-1 rounded bg-slate-800 text-slate-400 hover:text-white font-medium" data-filter="success">200 OK</button>
                    <button onclick="filterAuditLogs('error')" class="log-filter-btn px-2.5 py-1 rounded bg-slate-800 text-slate-400 hover:text-white font-medium" data-filter="error">Errors</button>
                </div>
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
                    <tbody id="audit-table-body">
                        {log_rows if log_rows else '<tr><td colspan="7" class="text-center py-8 text-slate-500 text-sm">No tool invocations recorded yet.</td></tr>'}
                    </tbody>
                </table>
            </div>
        </div>
    </main>

    <!-- Client-Side Search, Filter & Auto-Refresh Logic -->
    <script>
      // Prefix fixing for reverse proxy / ngrok
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

      // Tool Explorer Data
      const masterTools = {all_tools_json};
      let currentDomainFilter = 'all';
      const container = document.getElementById('tool-cards-container');

      function renderToolCards(tools) {{
        if (!container) return;
        if (tools.length === 0) {{
          container.innerHTML = '<div class="col-span-3 text-center py-10 text-slate-500 text-xs">No tools matching your query.</div>';
          return;
        }}
        const domainColorMap = {{
          cma: 'text-purple-400 border-purple-500/20 bg-purple-500/10',
          optix: 'text-cyan-400 border-cyan-500/20 bg-cyan-500/10',
          ups_fds: 'text-blue-400 border-blue-500/20 bg-blue-500/10',
          datadog: 'text-pink-400 border-pink-500/20 bg-pink-500/10',
          confluence: 'text-emerald-400 border-emerald-500/20 bg-emerald-500/10',
          salesforce: 'text-amber-400 border-amber-500/20 bg-amber-500/10'
        }};

        let html = '';
        tools.forEach(t => {{
          const d = (t.domain || 'general').toLowerCase();
          const badgeClass = domainColorMap[d] || 'text-slate-400 border-slate-700 bg-slate-800';
          const schema = t.schema || {{}};
          const props = schema.properties || {{}};
          const propKeys = Object.keys(props);
          const reqs = schema.required || [];

          let paramTags = '';
          propKeys.slice(0, 4).forEach(k => {{
            const isReq = reqs.includes(k);
            const reqStar = isReq ? '<span class="text-rose-400">*</span>' : '';
            paramTags += `<span class="px-1.5 py-0.5 rounded text-[10px] font-mono bg-slate-900 border border-slate-800 text-slate-300">${{k}}${{reqStar}}</span> `;
          }});
          if (propKeys.length > 4) {{
            paramTags += `<span class="text-[10px] text-slate-500 font-mono">+${{propKeys.length - 4}} more</span>`;
          }}

          html += `
          <div class="p-3.5 rounded-xl bg-slate-950/70 border border-slate-800/80 hover:border-indigo-500/40 transition flex flex-col justify-between">
            <div>
              <div class="flex items-start justify-between gap-2 mb-1.5">
                <code class="font-mono text-xs font-semibold text-white hover:text-indigo-300 transition cursor-pointer" onclick="navigator.clipboard.writeText('${{t.name}}'); alert('Copied ${{t.name}}');" title="Click to copy">${{t.name}}</code>
                <span class="text-[9px] uppercase font-mono px-1.5 py-0.5 rounded border ${{badgeClass}} shrink-0">${{d}}</span>
              </div>
              <p class="text-[11px] text-slate-400 line-clamp-2 leading-relaxed mb-3">${{t.description || 'No description available.'}}</p>
            </div>
            <div class="pt-2 border-t border-slate-900 flex items-center gap-1 flex-wrap">
              ${{paramTags || '<span class="text-[10px] text-slate-600 italic">No parameters</span>'}}
            </div>
          </div>
          `;
        }});
        container.innerHTML = html;
      }}

      function filterTools() {{
        const q = (document.getElementById('tool-search')?.value || '').toLowerCase().trim();
        let filtered = masterTools;
        if (currentDomainFilter !== 'all') {{
          filtered = filtered.filter(t => (t.domain || '').toLowerCase() === currentDomainFilter);
        }}
        if (q) {{
          filtered = filtered.filter(t => {{
            const nameMatch = (t.name || '').toLowerCase().includes(q);
            const descMatch = (t.description || '').toLowerCase().includes(q);
            return nameMatch || descMatch;
          }});
        }}
        renderToolCards(filtered);
      }}

      function filterToolsByDomain(domain) {{
        currentDomainFilter = domain;
        document.querySelectorAll('.tool-filter-btn').forEach(btn => {{
          if (btn.getAttribute('data-domain') === domain) {{
            btn.className = 'tool-filter-btn px-2.5 py-1 rounded-md font-semibold text-white bg-indigo-600 transition';
          }} else {{
            btn.className = 'tool-filter-btn px-2.5 py-1 rounded-md font-medium text-slate-400 hover:text-white hover:bg-slate-800 transition';
          }}
        }});
        filterTools();
      }}

      document.getElementById('tool-search')?.addEventListener('input', filterTools);
      // Initial render of all tools
      renderToolCards(masterTools);

      // Audit Log Filtering
      function filterAuditLogs(type) {{
        document.querySelectorAll('.log-filter-btn').forEach(btn => {{
          if (btn.getAttribute('data-filter') === type) {{
            btn.className = 'log-filter-btn px-2.5 py-1 rounded bg-indigo-600 text-white font-medium';
          }} else {{
            btn.className = 'log-filter-btn px-2.5 py-1 rounded bg-slate-800 text-slate-400 hover:text-white font-medium';
          }}
        }});

        const rows = document.querySelectorAll('.audit-row');
        rows.forEach(r => {{
          const code = parseInt(r.getAttribute('data-code') || '200');
          if (type === 'all') {{
            r.style.display = '';
          }} else if (type === 'success') {{
            r.style.display = code < 400 ? '' : 'none';
          }} else if (type === 'error') {{
            r.style.display = code >= 400 ? '' : 'none';
          }}
        }});
      }}

      // Auto Refresh Countdown (15s)
      let countdown = 15;
      const countdownEl = document.getElementById('countdown');
      const toggleEl = document.getElementById('autorefresh-toggle');
      const pulseEl = document.getElementById('refresh-pulse');

      setInterval(() => {{
        if (toggleEl && toggleEl.checked) {{
          countdown--;
          if (countdownEl) countdownEl.innerText = countdown;
          if (countdown <= 0) {{
            window.location.reload();
          }}
        }} else {{
          if (pulseEl) pulseEl.className = 'w-2 h-2 rounded-full bg-slate-600';
          if (countdownEl) countdownEl.innerText = 'Paused';
        }}
      }}, 1000);

      toggleEl?.addEventListener('change', () => {{
        if (toggleEl.checked) {{
          countdown = 15;
          if (pulseEl) pulseEl.className = 'w-2 h-2 rounded-full bg-emerald-400 animate-ping';
        }} else {{
          if (pulseEl) pulseEl.className = 'w-2 h-2 rounded-full bg-slate-600';
          if (countdownEl) countdownEl.innerText = 'Paused';
        }}
      }});
    </script>
</body>
</html>"""

package com.portfolio.kpi.api;

import java.time.Instant;
import java.util.LinkedHashMap;
import java.util.Map;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping
public class KpiController {

    @GetMapping("/health")
    public Map<String, Object> health() {
        Map<String, Object> payload = new LinkedHashMap<>();
        payload.put("status", "ok");
        payload.put("service", "kpi-alert-java-mirror");
        payload.put("timestamp", Instant.now().toString());
        return payload;
    }

    @GetMapping("/v1/kpis/overview")
    public Map<String, Object> kpiOverview() {
        Map<String, Object> payload = new LinkedHashMap<>();
        payload.put("metric_date", "2025-10-31");
        payload.put("new_users", 142);
        payload.put("active_users", 1688);
        payload.put("paid_conversions", 79);
        payload.put("conversion_rate", 0.0556);
        payload.put("net_revenue_usd", 12490.22);
        payload.put("refund_rate", 0.031);
        return payload;
    }
}

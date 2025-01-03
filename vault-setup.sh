#!/bin/bash
vault secrets enable pki
vault write pki/root/generate/internal common_name="example.com" ttl="8760h"
vault write pki/config/urls issuing_certificates="http://vault.vault.svc.cluster.local:8200/v1/pki/ca" crl_distribution_points="http://vault.vault.svc.cluster.local:8200/v1/pki/crl"
vault write pki/roles/flask-app allowed_domains="example.com" allow_subdomains=true max_ttl="24h"

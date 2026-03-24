import sys, re
sys.path.insert(0, 'docs/hooks')
import method_meta

html = (
    '<div class="tabbed-set tabbed-alternate" data-tabs="1:2">'
    '<input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio" />'
    '<input id="__tabbed_1_2" name="__tabbed_1" type="radio" />'
    '<div class="tabbed-labels">'
    '<label for="__tabbed_1_1">Method 1</label>'
    '<label for="__tabbed_1_2">Method 2</label>'
    '</div>'
    '<div class="tabbed-content">'
    '<div class="tabbed-block">'
    '<!-- @method-meta versions=["1.2.0"] obsolete=true -->'
    '<p>Old</p>'
    '</div>'
    '<div class="tabbed-block">'
    '<!-- @method-meta versions=["1.2.0"] obsolete=false -->'
    '<p>New</p>'
    '</div>'
    '</div>'
    '</div>'
)

result = method_meta.on_page_content(html, None, None)
print("OK" if "ub-obsolete" in result else "FAIL")
for label in re.findall(r'<label[^>]*>.*?</label>', result):
    print(label)

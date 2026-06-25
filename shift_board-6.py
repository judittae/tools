# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: ShiftBoard
class ShiftFilter:
    def __init__(self, records):
        self.records = records
    
    def filter_by_status(self, status):
        return [r for r in self.records if r.get('status') == status]
    
    def filter_by_category(self, category):
        return [r for r in self.records if r.get('category') == category]
    
    def filter_by_tag(self, tag):
        tags = {item['tag'] for item in self.records}
        return [r for r in self.records if any(r.get('tags', {}).get(t) == True for t in tags)]
    
    def combine_filters(self, status=None, category=None, tags=None):
        filtered = self.records
        if status:
            filtered = [r for r in filtered if r.get('status') == status]
        if category:
            filtered = [r for r in filtered if r.get('category') == category]
        if tags:
            filtered = [r for r in filtered if any(r.get('tags', {}).get(t) == True for t in tags)]
        return filtered
